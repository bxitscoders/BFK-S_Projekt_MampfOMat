# 🍰 MampfOMat

## 📌 Projektbeschreibung

Der **MampfOMat** ist ein digitaler Backwaren-Automat, der im Rahmen eines Schulprojekts entwickelt wurde.  
Die Anwendung ermöglicht es Benutzern, Produkte auszuwählen, in einen Warenkorb zu legen und Bestellungen auszuführen – ähnlich einem Online-Shop, jedoch für einen physischen Automaten.

Ziel des Projekts war die Umsetzung einer vollständigen Anwendung mit Frontend, Backend und Datenbank unter Verwendung moderner Software-Engineering-Prinzipien.


## 🎯 Einsatzmöglichkeiten

Der MampfOMat kann beispielsweise eingesetzt werden in:

- 🏫 Schulen (schnelle Pausenversorgung)  
- 🏢 Büros (Snackversorgung zwischendurch)  
- 🏥 Krankenhäusern (für Besucher)  
- 🚉 Bahnhöfen (24/7 Verfügbarkeit)  

## 🛠️ Technologie-Stack

**Programmiersprache:** Python  

**Frontend:**  
- Tkinter (Desktop-GUI)

**Backend:**  
- Django REST Framework

**Datenbank:**  
- SQLite (Standard für Entwicklung)  
- optional: MySQL/MariaDB

**Architektur:**  
- MVC/MVVM-orientiert  
- REST API  
- SOLID-Prinzipien

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
├── config/
│ ├── manage.py
│ └── settings.py
├── api/
├── diagramme/        
├── Praesentation/
├── Retros/
├── requirements.txt        #Anforderungen
├── db.sqlite3              # Datenbank
├── db.py
├── urls.py
└── README.md               # Das hier


## Projekt starten

## ✅ Voraussetzungen

- Python 3.10 – 3.12
- pip installiert

❗ Es werden keine externen Datenbank-Tools benötigt (SQLite wird automatisch verwendet).

## 1. Repository klonen

git clone https://github.com/bxitscoders/BFK-S_Projekt_MampfOMat.git
cd BFK-S_Projekt_MampfOMat

##  2. Virtuelle Umgebung erstellen & aktivieren

python -m venv .venv
.venv\Scripts\activate

##  3. Abhängigkeiten installieren

pip install -r requirements.txt

##  4. Datenbank initialisieren

cd config
python manage.py migrate
  ->Dieser Schritt erstellt automatisch alle benötigten Tabellen.

##  5. Datenbank initialisieren

python manage.py runserver
API erreichbar unter:
http://127.0.0.1:8000/

##  6. Frontend starten

cd Frontend
python main.py
  ->Die grafische Oberfläche startet anschließend automatisch.


## REST API Endpunkte
## Produkte

GET /api/produkte/
GET /api/produkte/<id>/
POST /api/produkte/
PUT /api/produkte/<id>/
DELETE /api/produkte/<id>/

## Bestellungen

GET /api/bestellungen/
GET /api/bestellungen/<id>/
POST /api/bestellungen/
PUT /api/bestellungen/<id>/
DELETE /api/bestellungen/<id>/


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

## Was wir gelernt haben

- Python GUIs sind nicht so schlecht wie alle sagen
- Bilder richtig zu skalieren ist nervig
- Ein gutes Design braucht Zeit
- SQLite reicht für fast alles aus
- Teamwork funktioniert besser mit Git
- MariaDB im zusammenhang mit Xampp funktioniert nicht gut
- Keine leeren Passwörter vergeben

## Team

**Oliver** - Rest API
**Beria** - Datenbanken + Backend
**Mert** - Frontend + Backend
**Nico** - Frontend + Backend

## Erfüllte Projektanforderungen

✅ CRUD-Operationen
✅ REST-API
✅ MVC/MVVM-Struktur
✅ Git-Versionierung
✅ SCRUM-Arbeitsweise
✅ SOLID-Prinzipien
✅ Projektdokumentation

## Mögliche Erweiterungen

- Online-Bezahlung
- Verkaufsstatistiken
- Mobile App
- Mehrsprachigkeit

-> Bei Fragen zum Projekt bitte das Entwicklerteam kontaktieren.

### Optional: Neue Migrations erstellen
Falls das Datenmodell geändert wird:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Datenbank-Optionen
- **Standard**: SQLite (db.sqlite3) - funktioniert sofort, keine weitere Konfiguration nötig
- **Optional**: MySQL/MariaDB - für den Produktivbetrieb empfohlen, benötigt zusätzliche Konfiguration

Die `setup.sql` ist für manuelles MySQL-Import (veraltet), verwende lieber `python manage.py migrate`.