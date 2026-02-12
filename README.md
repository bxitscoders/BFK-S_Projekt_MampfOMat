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


## Schnellstart

- Abhängigkeiten aus `requirements.txt` instalieren.

**Option 1: Frontend (GUI mit Tkinter)**

```bash
git clone https://github.com/bxitscoders/BFK-S_Projekt_MampfOMat.git
cd BFK-S_Projekt_MampfOMat
.venv\Scripts\Activate
pip install -r requirements.txt
cd Frontend
python main.py
```

**Option 2: Backend (Django REST API)**

```bash
git clone https://github.com/bxitscoders/BFK-S_Projekt_MampfOMat.git
cd BFK-S_Projekt_MampfOMat
.venv\Scripts\Activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Die API läuft dann auf `http://127.0.0.1:8000/`

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

## Setup für Backend-Entwicklung

### 1. Virtuelle Umgebung aktivieren
```bash
.venv\Scripts\Activate
```

### 2. Dependencies installieren
```bash
pip install -r requirements.txt
```

### 3. Datenbank initialisieren
```bash
python manage.py migrate
```
Dieser Befehl wendet alle Migrationen an und erstellt die Datenbanktabellen.

### 4. Django-Entwicklungsserver starten
```bash
python manage.py runserver
```
Die API läuft dann unter `http://127.0.0.1:8000/`

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

## REST API Endpunkte

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

