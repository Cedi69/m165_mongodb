import pymongo

# verbindung zur MongoDB herstellen

client = pymongo.MongoClient("mongodb://localhost:27017/")  
# MongoDB Verbindung

# Datenbank und sammlung auswählen 
db = client["spiele"]
collection = db["pcgames"]

def anzeigen():
    print("Alle Spiele in der Sammlung:")
    for spiel in collection.find({}, {'_id': 0}):
        print(spiel)
    print()



def einfuegen():
    print("Geben Sie die Informationen für das neue Spiel ein:")

    titel = input("Titel: ")

    ausgabejahr = int(input("Ausgabejahr: "))

    downloadzahlen = int(input("Downloadzahlen: "))

    altersgrenze = int(input("Altersgrenze: "))

    art = input("Art (kommagetrennt, z.B. 'RPG, Abenteuer'): ").split(', ')

    wertung = input("Wertung: ")
    


    neues_spiel = {
        "titel": titel,
        "ausgabejahr": ausgabejahr,
        "downloadzahlen": downloadzahlen,
        "altersgrenze": altersgrenze,
        "art": art,
        "wertung": wertung
    }

    collection.insert_one (neues_spiel)
    print (f"Neues Spiel eingefügt: {titel} ")
    anzeigen()



def finden(kriterium, wert):
    query = {kriterium: wert}
    gefundenes_spiel = collection.find_one (query, {'_id': 0})
    
    if gefundenes_spiel:
        print(f"Gefundenes Spiel mit {kriterium} = {wert}:")
        print(gefundenes_spiel)
    else:
        print(f"Kein Spiel mit {kriterium} = {wert} gefunden." )


def aendern():
    titel = input("Geben Sie den Titel des Spiels ein, das Sie ändern möchten: ")
    query = {"titel": titel}
    spiel = collection.find_one(query)

    if spiel:
        print("Aktuelle Informationen für das Spiel:")
        print(spiel)

        print("Geben Sie die neuen Informationen für das Spiel ein:")
        wertung = input("Neue Wertung: ")
        neue_daten = {"wertung": wertung}

        collection.update_one(query, {"$set": neue_daten})
        print(f"Daten aktualisiert für {titel}")
        anzeigen()
    else:
        print(f"Spiel mit dem Titel '{titel}' wurde nicht gefunden.")


def loeschen():
    titel = input("Geben Sie den Titel des Spiels ein, das Sie löschen möchten: ")
    query = {"titel": titel}
    spiel = collection.find_one(query)

    if spiel:
        collection.delete_one(query)
        print(f"Spiel gelöscht: {titel}")
        anzeigen()
    else:
        print(f"Spiel mit dem Titel '{titel}' wurde nicht gefunden.")



while True:
    print("Optionen:")
    print("1. Alle Spiele anzeigen")
    print("2. Spiele filtern")
    print("3. Neues Spiel hinzufügen")
    print("4. Spiel-Daten ändern")
    print("5. Spiel löschen")
    print("6. Beenden")

    auswahl = input("Ihre Auswahl: ")

    if auswahl == "1":
        anzeigen()
    elif auswahl == "2":
        kriterium = input("Geben Sie das Kriterium ein (z.B 'titel', 'ausgabejahr', 'art'): ")
        wert = input(f"Geben Sie den Wert für {kriterium} ein: ")
        finden(kriterium, wert)
    elif auswahl == "3":
        einfuegen()
    elif auswahl == "4":
        aendern()
    elif auswahl == "5":
        loeschen()
    elif auswahl == "6":
        break
    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine der Optionen (1-6).")



# verbindung  wird zu MongoDB geschlossen
client.close()

