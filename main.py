from threading import Event
from configuration.configuration import configuration

print("Dienst läuft...")

# Configuration laden in Objekt
config = configuration()
config.load_config()

Event().wait()