import abc
import datetime
from typing import Any

from azairnotifier.application.value import FlightSearch


class FlightSearchRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, pk: str) -> FlightSearch:
        pass

    @abc.abstractmethod
    def find_one_by(self, fields: dict[str, Any]) -> FlightSearch:
        pass

    @abc.abstractmethod
    def find_before_date(self, date: datetime.datetime) -> list[FlightSearch]:
        pass

    @abc.abstractmethod
    def save(self, flight_search: FlightSearch) -> str:
        pass

    @abc.abstractmethod
    def update(self, pk: str, flight_search: FlightSearch) -> None:
        pass

    @abc.abstractmethod
    def delete(self, unsubscribe_code: str) -> None:
        pass
