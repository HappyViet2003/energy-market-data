from dataclasses import dataclass
import datetime


@dataclass
class StromMesswert:
    timestamp: datetime
    filter_id: str
    region: str
    resolution: str
    value: float
