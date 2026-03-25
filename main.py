from threading import Event
from Configuration.Configuration import Configuration
from Services.DataAquisition import DataAquisition
from Services.DatabaseService import DatabaseService

print("Dienst läuft...")

# Configuration laden in Objekt
config = Configuration()

# TODO Hier Datenbankverbindung aufbauen
db = DatabaseService(config=config)

# Daten laden und verarbeiten und abschließend in DB speichern
dataAquisition = DataAquisition(config=config, dbService=db)

Event().wait()
