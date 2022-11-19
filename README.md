# GEM PDF GENERÁTOR

## Telepítés

Keressünk egy számunkra kedves mappát, esetleg hozzunk létre egy újat. A projekt teljes tartalmát másoljuk bele.

Nyissunk meg egy parancssort és navigáljunk el az előbb kiválasztott mappához. 

Írjuk be az alábbiakat a parancssorba:

```bash
python -m venv .venv & pip install -r requirements.txt
```

Ha az előbbi lépéssel megvagyunk, már használhatjuk is a kedvenc dokumentum generátorunkat.

Használat:

```bash
python main.py <sablon_fájl> <adat_csv>
```

Példaként próbáljuk ki:

```bash
python main.py example.xml test.csv
```

## Javaslom, hogy a két felhasznált fájlt tegyük be a main.py mellé

## A kimenet xml formátumban megtalálható lesz a ./output mappában

