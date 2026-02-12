# 🍰 MampfOMat

## Was ist das hier?

Das MampfOMat ist ein Automat für Backwaren, den wir als Schulprojekt entwickelt haben. Die Idee ist simpel: Du gehst hin, wählst aus was du möchtest, packst es in den Warenkorb und kaufst es. Wie ein Online-Shop, nur für einen echten Automaten.

Wir dachten uns, dass es praktisch wäre wenn man nicht immer anstehen muss, besonders in der Schule wo die Pausen kurz sind.

## Wo könnte man das brauchen?

**In der Schule** - das war unser erster Gedanke. Schnell was holen ohne Warteschlange.

**Im Büro** - wenn die Kantine zu hat oder man Hunger zwischendurch hat.

**Krankenhäuser** - für Besucher die lange warten müssen.

**Bahnhöfe** - wenn alles andere schon zu ist.

Eigentlich überall wo Leute mal schnell was zu essen brauchen.

## Wie funktioniert das technisch?

Wir haben das ganze in **Python** gemacht, weil wir das am besten können und es auf jedem Computer läuft.

**Frontend:** Tkinter - sieht aus wie eine normale App, nichts besonderes aber funktioniert gut

**Backend:** Ist direkt in Python mit drin, keine komplizierten Server oder so

**Datenbank:** SQLite für die Entwicklung, später MySQL wenn es ernst wird

**Design:** Haben versucht es wie WhatsApp aussehen zu lassen, weil das jeder kennt

## Projektstruktur


MampfOMat/
├── Frontend/
│   ├── main.py              # Hier startet alles
│   ├── ui/
│   │   ├── app.py           # Hauptfenster
│   │   ├── home_page.py     # Produktliste
│   │   ├── product_page.py  # Einzelprodukt
│   │   ├── cart_page.py     # Warenkorb
│   │   ├── admin_page.py    # Für neue Produkte
│   │   └── modern_styles.py # Farben und Schriften
│   └── assets/              # Bilder
├── db.sqlite3              # Datenbank
└── README.md               # Das hier


## Ausprobieren

Du brauchst:
- Python (3.7 oder neuer)
- Pillow für die Bilder: `pip install pillow`

Dann einfach:

git clone https://github.com/bxitscoders/BFK-S_Projekt_MampfOMat.git
cd BFK-S_Projekt_MampfOMat/Frontend
python main.py

Für die DB: 
XAMPP starten ->  Apache und MySQL starten ->  http://localhost/phpmyadmin/ -> Importieren klicken -> setup.sql Datei wählen - > OK --> Datenbank mampf


Das wars schon.

## Was wir gelernt haben

- Python GUIs sind nicht so schlecht wie alle sagen
- Bilder richtig zu skalieren ist nervig
- Ein gutes Design braucht Zeit
- SQLite reicht für fast alles aus
- Teamwork funktioniert besser mit Git

## Team

**Oliver** - Rest API
**Beria** - Datenbanken
**Mert** - Frontend + Backend
**Nico** - Frontend + Backend

## Projekt-Anforderungen

Mussten wir für die Schule machen:
- ✅ CRUD (Erstellen, Lesen, Ändern, Löschen)
- ✅ MVC Architektur  
- ✅ Dokumentation
- ✅ Git/SCRUM
- ✅ S.O.L.I.D Prinzipien

## Was noch kommen könnte

- Echte Bezahlung
- Statistiken welche Sachen am besten laufen  
- Handy App zum Vorbestellen
- Mehrere Sprachen



Falls Fragen sind oder was nicht läuft, einfach melden. 

---

## Installationen:

Damit django richtig funktioniert wurde ein requiremnets.txt erstellt. In dieser sind die Dependencies hinterlegt.

Die Dependencies werden aus dem root projekt Verzeichniss installiert.

$ .venv\Scripts\Activate

$ cd <root prject>

$ pip install -r requirements.txt

Wenn die Datenbak eingerichtet werden muss:

$ python manage.py makemigrations

$ python manage.py migrate

Um runserver zu starten:

$ cd config

$ python .\manage.py runserver

## REST API Endpunkte

### PowerShell Befehle

#### GET - Alle Produkte anzeigen
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/produkte/" | Select-Object -ExpandProperty Content
```

#### GET - Einzelnes Produkt (ID=1)
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/produkte/1/" | Select-Object -ExpandProperty Content
```

#### POST - Neues Produkt erstellen
```powershell
$body = @{ 
    name="Pizza Margherita"
    beschreibung="Klassische Pizza mit Mozzarella und Basilikum"
    preis=12.99 
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/produkte/" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

#### DELETE - Produkt löschen (ID=1)
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/produkte/1/" -Method DELETE
```

#### POST - Neue Bestellung erstellen
```powershell
$body = @{ 
    produkt=1
    menge=2
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/bestellungen/" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

#### GET - Alle Bestellungen anzeigen
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/bestellungen/" | Select-Object -ExpandProperty Content
```

#### DELETE - Bestellung löschen (ID=1)
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/bestellungen/1/" -Method DELETE
```

---

### Datenbank überprüfen

#### Alle Produkte anzeigen (Django Shell)
```powershell
cd c:\Users\O5H\OneDrive -it.schule Stuttgart\Dokumente\Projekt\BFK-S_Projekt_MampfOMat
.\.venv\Scripts\python config\manage.py shell
```

Dann in der Shell:
```python
from api.models import Product
for p in Product.objects.all():
    print(f"ID: {p.id}, Name: {p.name}, Preis: {p.preis}€, Beschreibung: {p.beschreibung}")
```

#### Alle Bestellungen anzeigen 
```python
from api.models import Order
for o in Order.objects.all():
    print(f"ID: {o.id}, Produkt: {o.produkt.name}, Menge: {o.menge}, Timestamp: {o.timestamp}")
```

#### Produkt-Anzahl zählen
```python
from api.models import Product, Order
print(f"Produkte: {Product.objects.count()}")
print(f"Bestellungen: {Order.objects.count()}")
```

#### Datenbank leeren (Vorsicht!)
```python
from api.models import Product, Order
Product.objects.all().delete()
Order.objects.all().delete()
print("Datenbank geleert!")
```

#### Aus der Shell zurück zur PowerShell
```python
exit()
```



### REST API Endpunkte Übersicht

**Produkte:**
- `GET /api/produkte/` - Alle Produkte
- `GET /api/produkte/<id>/` - Einzelnes Produkt
- `POST /api/produkte/` - Neues Produkt erstellen
- `PUT /api/produkte/<id>/` - Produkt bearbeiten
- `DELETE /api/produkte/<id>/` - Produkt löschen

**Bestellungen:**
- `GET /api/bestellungen/` - Alle Bestellungen
- `GET /api/bestellungen/<id>/` - Einzelne Bestellung
- `POST /api/bestellungen/` - Neue Bestellung erstellen
- `PUT /api/bestellungen/<id>/` - Bestellung bearbeiten
- `DELETE /api/bestellungen/<id>/` - Bestellung löschen

