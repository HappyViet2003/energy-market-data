import yaml
import os


class Configuration:
    def __init__(self):
        self.url = None
        self.filter = None
        self.region = None
        self.resolution = None

        self.load_config()

    def load_config(self):
        print("Konfiguration wird geladen...")

        # Pfad-Check für Docker vs lokal
        config_path = "/app/config.yaml"
        if not os.path.exists(config_path):
            config_path = "Configuration/example/config.yaml"

        try:
            with open(config_path, "r") as file:
                config = yaml.safe_load(file)
                self.url = config.get("url").rstrip("/")
                self.filter = config.get("filter")
                self.region = config.get("region")
                self.resolution = config.get("resolution")
                print(f"URL geladen: {self.url}")
        except FileNotFoundError:
            print(f"Fehler: Konfigurationsdatei nicht gefunden unter {config_path}")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
