from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.configuration import Configuration
import os
from datetime import datetime
from Models.StromMesswert import StromMesswert


class DatabaseService:
    def __init__(self, config: Configuration):
        self.config = config
        self.client = None
        self.bucket = os.environ["INFLUXDB_BUCKET"]
        self.org = os.environ["INFLUXDB_ORG"]
        self.connect()

    def connect(self):
        print("Datenbankverbindung wird aufgebaut...")
        self.client = InfluxDBClient(
            url=os.environ["INFLUXDB_URL"],
            token=os.environ["INFLUXDB_TOKEN"],
            org=self.org,
        )
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()

    # ── private Hilfsmethode ──────────────────────────────────────────
    def _parse(self, result) -> list[StromMesswert]:
        return [
            StromMesswert(
                timestamp=record.get_time(),
                filter_id=record.values["filter"],
                region=record.values["region"],
                resolution=record.values["resolution"],
                value=record.get_value(),
            )
            for table in result
            for record in table.records
        ]

    def _query(
        self,
        filter_id: str = None,
        region: str = None,
        resolution: str = None,
        stunden: int = 24,
    ) -> list[StromMesswert]:
        filter_zeilen = ['|> filter(fn: (r) => r._measurement == "strom")']
        if filter_id:
            filter_zeilen.append(f'|> filter(fn: (r) => r.filter == "{filter_id}")')
        if region:
            filter_zeilen.append(f'|> filter(fn: (r) => r.region == "{region}")')
        if resolution:
            filter_zeilen.append(
                f'|> filter(fn: (r) => r.resolution == "{resolution}")'
            )

        query = (
            f'from(bucket: "{self.bucket}")\n'
            f"|> range(start: -{stunden}h)\n" + "\n".join(filter_zeilen)
        )
        return self._parse(self.query_api.query(query))

    # ── public API ───────────────────────────────────────────────────
    def schreibe(
        self,
        timestamp: datetime,
        filter_id: str,
        region: str,
        resolution: str,
        value: float,
    ):
        point = (
            Point("strom")
            .tag("filter", filter_id)
            .tag("region", region)
            .tag("resolution", resolution)
            .field("value", value)
            .time(timestamp)
        )
        self.write_api.write(bucket=self.bucket, record=point)

    def schreibe_batch(self, messwerte: list[StromMesswert]):
        points = [
            Point("strom")
            .tag("filter", m.filter_id)
            .tag("region", m.region)
            .tag("resolution", m.resolution)
            .field("value", m.value)
            .time(m.timestamp)
            for m in messwerte
        ]
        self.write_api.write(bucket=self.bucket, record=points)

    def lese(
        self, filter_id: str, region: str, resolution: str, stunden: int = 24
    ) -> list[StromMesswert]:
        return self._query(filter_id, region, resolution, stunden)

    def lese_alle(
        self, region: str, resolution: str, stunden: int = 24
    ) -> list[StromMesswert]:
        return self._query(region=region, resolution=resolution, stunden=stunden)

    def close(self):
        if self.client:
            self.client.close()
