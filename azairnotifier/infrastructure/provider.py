import json
from typing import override
from azairnotifier.application.provider import AirportsProvider


class JsonFileAirportsProvider(AirportsProvider):
    def __init__(self, path: str):
        self.path = path

    @override
    def get_airports(self) -> dict:
        with open(self.path) as file:
            return json.load(file)
