# engeto-projekt-3
# Elections Scraper


**Popis projektu**

Tento projekt slouží k extrahování výsledků parlamentních voleb z roku 2017. Odkaz na web naleznete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).


**Instalace knihoven**

Použité knihovny jsou uvedeny v souboru "**requirements.txt**". Pro jejich instalaci využijte package manager "**pip3**".

```python
pip3 install -r requirements.txt   #nainstaluje knihovny
```

**Spuštění projektu**

Pro spuštění souboru "**main.py**" zadejte 2 povinné argumenty v uvedeném pořadí.

```python
python main.py <URL-odkaz-uzemniho-celku> <vysledny_CSV_soubor>
```
Následně se vám stáhnou výsledky jako soubor s příponou ".**csv**".

**Ukázka projektu**

Výsledky hlasování pro okres Benešov:

1. argument - https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. argument - outfile.csv

Spuštění programu:
```python
python C:\git_repository\engeto-projekt-3\main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" outfile.csv
```

Průběh stahování:

```python
"Spouštím web scraper a stahuji data z vybraného volebního okrsku.."
"Kód obce: 529303, Název obce: Benešov"
"Kód obce: 532568, Název obce: Bernartice"
"Kód obce: 530743, Název obce: Bílkovice"
"Kód obce: 532380, Název obce: Blažejovice"
"Kód obce: 532096, Název obce: Borovnice"
"..."
"..."
"Web scraping byl úspěšně dokončen. Výsledky jsou uloženy v souboru outfile.csv"
```