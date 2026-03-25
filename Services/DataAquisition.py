from datetime import datetime, timezone
import requests
from Configuration.Configuration import Configuration
from Models.StromMesswert import StromMesswert
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

            latest_timestamp = data["timestamps"][-1]

            # f"https://www.smard.de/app/chart_data/4169/DE/4169_DE_quarterhour_{latest_timestamp}.json"

            live_url = f"{self.config.url}/{self.config.filter}/{self.config.region}/{self.config.filter}_{self.config.region}_{self.config.resolution}_{latest_timestamp}.json"

            live_response = requests.get(live_url)

            live_response.raise_for_status()

            live_data = live_response.json()

            serie = live_data.get("series", [])

            messwerte = []

            for eintrag in serie:
                timestamp_ms, wert = eintrag

                if wert is None:
                    continue

                messwerte.append(
                    StromMesswert(
                        timestamp=datetime.fromtimestamp(
                            timestamp_ms / 1000, tz=timezone.utc
                        ),
                        filter_id=self.config.filter,
                        region=self.config.region,
                        resolution=self.config.resolution,
                        value=float(wert),
                    )
                )

            if messwerte:
                self.dbService.schreibe_batch(messwerte)
                print(f"{len(messwerte)} Messwerte gespeichert.")

            print("Live Daten erfolgreich akquiriert.")

        except requests.exceptions.RequestException as e:
            print(f"Fehler bei der Datenakquisition: {e}")
            return None
        except ValueError:
            print("Fehler: Antwort ist kein gültiges JSON.")
            return None
