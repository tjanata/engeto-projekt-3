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

Pro spuštění souboru "**main.py**" zadejte 2 povinné argumenty.

```python
python main.py <URL-odkaz-uzemniho-celku> <vysledny_CSV_soubor>
```