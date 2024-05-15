import unittest
import datetime
from unittest.mock import patch, MagicMock
from azairnotifier.application.value import FlightSearch
from azairnotifier.infrastructure.handler.queryhandler import GetFlightSearchesByParametersQueryHandler, \
    GetFlightSearchesBeforeGivenDateQueryHandler
from azairnotifier.infrastructure.repository import FlightSearchRepository
from tests.data_provider import provide


class TestGetFlightSearchesBeforeGivenDateParametersQueryHandler(unittest.TestCase):
    @patch('azairnotifier.application.repository.FlightSearchRepository')
    @provide([(
            'unsubscribeCode',
            [FlightSearch.from_dict({'email': 'test@test.pl', 'next_search': datetime.datetime.now(), 'parameters': [], 'unsubscribe_code': 'unsubscribeCode'})]
        )]
    )
    def test_it_should_return_all_flight_search_results_before_given_date(
            self,
            repository: FlightSearchRepository,
            _date: datetime.datetime,
            flight_searches: list[FlightSearch]
    ) -> None:
        repository.find_before_date = MagicMock(return_value=flight_searches)

        handler = GetFlightSearchesBeforeGivenDateQueryHandler(repository)
        result = handler.get(_date)
        repository.find_before_date(_date)
        self.assertEqual(result, flight_searches)