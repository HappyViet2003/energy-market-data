from threading import Event
from Configuration.Configuration import Configuration
from Services.DataAquisition import DataAquisition

print("Dienst läuft...")

# Configuration laden in Objekt
config = Configuration()

# Daten laden und verarbeiten und abschließend in DB speichern
dataAquisition = DataAquisition(config=config)

Event().wait()
