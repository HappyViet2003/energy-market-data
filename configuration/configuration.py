import yaml
import os

class configuration:
    def __init__(self):
        self.url = None

    def load_config(self):
        print("Konfiguration wird geladen...")

        # Pfad-Check für Docker vs lokal
        config_path = "/app/config.yaml"
        if not os.path.exists(config_path):
            config_path = "configuration/example/config.yaml"

        try:
            with open(config_path, "r") as file:
                config = yaml.safe_load(file)
                self.url = config.get("url")
                print(f"URL geladen: {self.url}")
        except FileNotFoundError:
            print(f"Fehler: Konfigurationsdatei nicht gefunden unter {config_path}")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

