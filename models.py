from dataclasses import dataclass
from typing import Dict


@dataclass
class EventSchema:
    type: str
    features: Dict

@dataclass
class ApiResponse:
    countries: Dict
    events: EventSchema