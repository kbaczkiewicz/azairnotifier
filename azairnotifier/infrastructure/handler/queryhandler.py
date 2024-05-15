from datetime import datetime

from azairnotifier.application.handler.queryhandler import \
    GetFlightSearchesQueryHandler as GetFlightSearchesQueryHandlerInterface, \
    GetFlightSearchesByParametersQueryHandler as GetFlightSearchesByParametersQueryHandlerInterface, \
    GetFlightSearchesBeforeGivenDateQueryHandler as GetFlightSearchesBeforeGivenDateQueryHandlerInterface
from azairnotifier.application.repository import FlightSearchRepository
from azairnotifier.application.value import FlightSearch


class GetFlightSearchesQueryHandler(GetFlightSearchesQueryHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        self.repository = repository

    def get_by_pk(self, pk: str) -> FlightSearch:
        return self.repository.get(pk)


class GetFlightSearchesByParametersQueryHandler(GetFlightSearchesByParametersQueryHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        self.repository = repository

    def get_by_email(self, email: str) -> FlightSearch:
        return self.repository.find_one_by({'email': email})

    def get_by_unsubscribe_code(self, unsubscribe_code: str):
        return self.repository.find_one_by({'unsubscribe_code': unsubscribe_code})


class GetFlightSearchesBeforeGivenDateQueryHandler(GetFlightSearchesBeforeGivenDateQueryHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        self.repository = repository

    def get(self, date: datetime) -> list[FlightSearch]:
        return self.repository.find_before_date(date)



