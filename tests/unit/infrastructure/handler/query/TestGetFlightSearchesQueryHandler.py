import datetime
import unittest
from unittest.mock import patch, MagicMock

from azairnotifier.application.repository import FlightSearchRepository
from azairnotifier.application.value import FlightSearch
from azairnotifier.infrastructure.handler.queryhandler import GetFlightSearchesQueryHandler
from tests.data_provider import provide


class GetFlightSearchesQueryHandlerTest(unittest.TestCase):
    @patch('azairnotifier.application.repository.FlightSearchRepository')
    @provide([(FlightSearch.from_dict({'email': 'test@test.pl', 'next_search': datetime.datetime.now(), 'parameters': [], 'unsubscribe_code': 'unsubscribeCode'}),)])
    def test_returns_flight_search(self, flight_search_repository: FlightSearchRepository, flight_search: FlightSearch) -> None:
        flight_search_repository.get = MagicMock(return_value=flight_search)
        handler = GetFlightSearchesQueryHandler(flight_search_repository)
        result = handler.get_by_pk('id-1')
        flight_search_repository.get.assert_called_once_with('id-1')
        self.assertEqual(result, flight_search)

    @patch('azairnotifier.application.repository.FlightSearchRepository')
    @provide([(None,)])
    def test_returns_none_on_empty_flight_search(self, flight_search_repository: FlightSearchRepository, data: dict) -> None:
        flight_search_repository.get = MagicMock(return_value=data)
        handler = GetFlightSearchesQueryHandler(flight_search_repository)
        result = handler.get_by_pk('id-1')
        flight_search_repository.get.assert_called_once_with('id-1')
        self.assertIsNone(result)