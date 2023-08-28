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
<pre>
python C:\git_repository\engeto-projekt-3\main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" outfile.csv
</pre>

Průběh stahování:

<pre>
Spouštím web scraper a stahuji data z vybraného volebního okrsku..
Kód obce: 529303, Název obce: Benešov
Kód obce: 532568, Název obce: Bernartice
Kód obce: 530743, Název obce: Bílkovice
Kód obce: 532380, Název obce: Blažejovice
Kód obce: 532096, Název obce: Borovnice
...
...
Web scraping byl úspěšně dokončen. Výsledky jsou uloženy v souboru outfile.csv
</pre>

Část výstupu:

<pre>
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,...
529303,Benešov,13 104,8 485,8 437,1 052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2 577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
</pre>