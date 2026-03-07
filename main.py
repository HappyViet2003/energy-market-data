from threading import Event
from Configuration.Configuration import Configuration

print("Dienst läuft...")

# Configuration laden in Objekt
config = Configuration()

Event().wait()