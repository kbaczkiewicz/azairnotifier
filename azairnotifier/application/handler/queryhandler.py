import abc
import datetime
import datetime

from azairnotifier.application.value import FlightSearch


class GetFlightSearchesQueryHandler(abc.ABC):
    @abc.abstractmethod
    def get_by_pk(self, pk: str) -> FlightSearch:
        pass


class GetFlightSearchesByParametersQueryHandler(abc.ABC):
    @abc.abstractmethod
    def get_by_email(self, email: str) -> FlightSearch:
        pass

    @abc.abstractmethod
    def get_by_unsubscribe_code(self, unsubscribe_code: str) -> FlightSearch:
        pass


class GetFlightSearchesBeforeGivenDateQueryHandler(abc.ABC):
    @abc.abstractmethod
    def get(self, date: datetime.datetime) -> list[FlightSearch]:
        pass
