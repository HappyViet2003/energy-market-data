import requests
from Configuration.Configuration import Configuration
from Services.DatabaseService import DatabaseService


class DataAquisition:
    def __init__(self, config: Configuration, dbService: DatabaseService):
        self.config = config
        self.dbService = dbService

        self.acquire_data()

    def acquire_data(self):
        print("Daten werden akquiriert...")
        try:
            # url: "https://www.smard.de/app/chart_data/4169/DE/index_quarterhour.json"

            # Aktuellsten verfügbaren Zeitstempel abrufen
            fullUrl = f"{self.config.url}/{self.config.filter}/{self.config.region}/index_{self.config.resolution}.json"
            print(fullUrl)

            response = requests.get(fullUrl)
            response.raise_for_status()

            data = response.json()
            print("Daten erfolgreich akquiriert.")

            # Nun echte Daten holen, da der Zeitstempel bekannt ist
            # TODO Weiter bearbeiten

            latest_timestamp = data["timestamps"][-1]

            # f"https://www.smard.de/app/chart_data/4169/DE/4169_DE_quarterhour_{latest_timestamp}.json"

            live_url = f"{self.config.url}/{self.config.filter}/{self.config.region}/{self.config.filter}_{self.config.region}_{self.config.resolution}_{latest_timestamp}.json"

            live_response = requests.get(live_url)

            live_response.raise_for_status()

            live_data = live_response.json()

            print("Live Daten erfolgreich akquiriert.")

        except requests.exceptions.RequestException as e:
            print(f"Fehler bei der Datenakquisition: {e}")
            return None
        except ValueError:
            print("Fehler: Antwort ist kein gültiges JSON.")
            return None
