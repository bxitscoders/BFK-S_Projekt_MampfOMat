import mysql.connector

# Verbindung herstellen
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Mampf"
)

cursor = conn.cursor()

print("Verbindung zur Datenbank erfolgreich!")

# produkte abrufen
cursor.execute("SELECT * FROM produkte")


produkte = cursor.fetchall()


for p in produkte:
    print(f"ID: {p[0]}, Name: {p[1]}, Preis: {p[2]}€, Beschreibung: {p[3]}")

cursor.close()
conn.close()