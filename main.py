"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Tomas Janata
email: tomas.janata@nempk.cz
discord: TomášJ#3088
"""

#Import libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import csv


#Function for validation of URL address
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


#Function for write header to CSV file
def write_headers_to_csv(csv_writer, values_list):
    csv_writer.writerow(values_list)


#Function for write data to CSV file
def write_data_to_csv(csv_writer, items_list):
    csv_writer.writerow(items_list)


#Function for get name of political parties and save to CSV
def get_party_names_from_subpage(subpage_url):
    response = requests.get(subpage_url)
    subpage_soup = BeautifulSoup(response.text, 'html.parser')

    party_names = []

    #Get name of political parties from first table
    parties_names_t1 = subpage_soup.find_all('td', class_='overflow_name', headers='t1sa1 t1sb2')
    for part in parties_names_t1:
        party_name = part.get_text(strip=True)
        party_names.append(party_name)

    #Get name of political parties from second table
    parties_names_t2 = subpage_soup.find_all('td', class_='overflow_name', headers='t2sa1 t2sb2')
    for part in parties_names_t2:
        party_name = part.get_text(strip=True)
        party_names.append(party_name)

    return party_names


#Function for scrapping data from subpages
def scrape_subpage_data(url, csv_writer, city_number, city_name):
    response = requests.get(url)
    subpage_soup = BeautifulSoup(response.text, 'html.parser')

    #Number of electorate in subpages
    electorate_element = subpage_soup.find('td', class_='cislo', headers='sa2', attrs={'data-rel': 'L1'})
    if electorate_element:
        electorate_value = electorate_element.get_text(strip=True)
    else:
        electorate_value = "N/A"

    #Number of envelope in subpages
    envelope_elements = subpage_soup.find_all('td', class_='cislo', headers='sa3', attrs={'data-rel': 'L1'})
    if envelope_elements:
        envelope_value = envelope_elements[0].get_text(strip=True)
    else:
        envelope_value = "N/A"

    #Number of valid vote in subpages
    valid_vote_elements = subpage_soup.find_all('td', class_='cislo', headers='sa6', attrs={'data-rel': 'L1'})
    if valid_vote_elements:
        valid_vote_value = valid_vote_elements[0].get_text(strip=True)
    else:
        valid_vote_value = "N/A"

    #Number of votes for all political parties in first table
    parties_data_t1 = subpage_soup.find_all('td', class_='overflow_name', headers='t1sa1 t1sb2')
    votes_data_t1 = subpage_soup.find_all('td', class_='cislo', headers='t1sa2 t1sb3')

    parties_votes_t1 = {}
    for ppart, votes in zip(parties_data_t1, votes_data_t1):
        parties_votes_t1[ppart.get_text(strip=True)] = votes.get_text(strip=True)

    # Number of votes for all political parties in second table
    parties_data_t2 = subpage_soup.find_all('td', class_='overflow_name', headers='t2sa1 t2sb2')
    votes_data_t2 = subpage_soup.find_all('td', class_='cislo', headers='t2sa2 t2sb3')

    parties_votes_t2 = {}
    for ppart, votes in zip(parties_data_t2, votes_data_t2):
        parties_votes_t2[ppart.get_text(strip=True)] = votes.get_text(strip=True)

    # Write data to CSV file
    row_data = [city_number, city_name, electorate_value, envelope_value, valid_vote_value]
    for ppart, votes in parties_votes_t1.items():
        row_data.append(votes)
    for ppart, votes in parties_votes_t2.items():
        row_data.append(votes)
    
    write_data_to_csv(csv_writer, row_data)


#Function for scrapping data from main URL
def scrape_and_save(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get city numbers and names
    city_rows = soup.find_all('tr')

    with open(output_file, 'a', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in city_rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                city_number = cells[0].get_text(strip=True)
                city_name = cells[1].get_text(strip=True)
                print(f"Kód obce: {city_number}, Název obce: {city_name}")  #Printing data to console

    
                subpage_link = cells[0].find('a')['href']  #Link on the subpage
                subpage_url = f"https://volby.cz/pls/ps2017nss/{subpage_link}"
                #Call function for subpage
                scrape_subpage_data(subpage_url, csv_writer, city_number, city_name)


# Main function
def main():
    separator = "-----------------------------------------------"
    header_list = []

    if len(sys.argv) != 3:
        print(f"Pro spuštění {sys.argv[0]} zadejte 2 povinné argumenty (v pořadí - URL adresa a název CSV výstupního souboru)")
        return

    elif not is_valid_url(sys.argv[1]):
        print(f"Zadaná adresa {sys.argv[1]} není platnou URL adresou")
        return

    elif not sys.argv[2].endswith(".csv"):
        print(f"Zadaný soubor {sys.argv[2]} není CSV soubor")
        return

    else:
        print(f"Spouštím web scraper..")

        # Get the first subpage link
        response = requests.get(sys.argv[1])
        main_page_soup = BeautifulSoup(response.text, 'html.parser')

        #Find the first subpage link
        subpage_link_element = main_page_soup.find('td', class_='cislo', headers='t1sa1 t1sb1').find('a', href=True)
        if subpage_link_element:
            subpage_link = subpage_link_element['href']
            subpage_url = f"https://volby.cz/pls/ps2017nss/{subpage_link}"

            #Call function for geting name of political parties from first subpage
            party_names_first_subpage = get_party_names_from_subpage(subpage_url)
            header_list.extend(["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"] + party_names_first_subpage)
        else:
            print("Odkaz na podstránku nebyl nalezen.")

        # Write header to CSV file
        with open(sys.argv[2], 'w', newline='', encoding='utf-8-sig') as csv_file:
            csv_writer = csv.writer(csv_file)
            write_headers_to_csv(csv_writer, header_list)

        # Call function for scraping data from main URL
        scrape_and_save(sys.argv[1], sys.argv[2])

        print(f"Web scraping byl úspěšně dokončen")
        print(separator)

if __name__ == '__main__':
    main()
