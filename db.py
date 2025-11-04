import mysql.connector

# Verbindung herstellen
conn = mysql.connector.connect(
    host="localhost",      # Servername (meist localhost)
    user="root",           # Benutzername (Standard bei XAMPP)
    password="",           # Passwort (oft leer)
    database="Mampf"       # Deine Datenbank
)

# Cursor zum Ausführen von SQL-Befehlen
cursor = conn.cursor()

print("Verbindung zur Datenbank erfolgreich!")

# Beispiel: Daten aus der Tabelle 'produkte' abrufen
cursor.execute("SELECT * FROM produkte")

# Alle Ergebnisse holen
produkte = cursor.fetchall()

# Ergebnisse ausgeben
for p in produkte:
    print(f"ID: {p[0]}, Name: {p[1]}, Preis: {p[2]}€, Beschreibung: {p[3]}")

# Verbindung schließen
cursor.close()
conn.close()