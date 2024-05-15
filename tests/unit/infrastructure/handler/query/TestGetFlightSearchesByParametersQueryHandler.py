import unittest
import datetime
from unittest.mock import patch, MagicMock
from azairnotifier.application.value import FlightSearch
from azairnotifier.infrastructure.handler.queryhandler import GetFlightSearchesByParametersQueryHandler
from azairnotifier.infrastructure.repository import FlightSearchRepository
from tests.data_provider import provide


class TestGetFlightSearchesByParametersQueryHandler(unittest.TestCase):
    @patch('azairnotifier.application.repository.FlightSearchRepository')
    @provide([(
            'test@test.pl',
            FlightSearch.from_dict({'email': 'test@test.pl', 'next_search': datetime.datetime.now(), 'parameters': [], 'unsubscribe_code': 'unsubscribeCode'})
        )]
    )
    def test_it_should_return_all_flight_search_results_with_given_email(
            self, repository: FlightSearchRepository,
            email: str,
            flight_search: FlightSearch
    ) -> None:
        repository.find_one_by = MagicMock(return_value=flight_search)

        handler = GetFlightSearchesByParametersQueryHandler(repository)
        result = handler.get_by_email(email)
        repository.find_one_by.assert_called_once_with({'email': email})
        self.assertEqual(result, flight_search)

    @patch('azairnotifier.application.repository.FlightSearchRepository')
    @provide([(
            'unsubscribeCode',
            FlightSearch.from_dict({'email': 'test@test.pl', 'next_search': datetime.datetime.now(), 'parameters': [], 'unsubscribe_code': 'unsubscribeCode'})
        )]
    )
    def test_it_should_return_all_flight_search_results_with_given_unsubscribe_code(
            self,
            repository: FlightSearchRepository,
            unsubscribe_code: str,
            flight_search: FlightSearch
    ) -> None:
        repository.find_one_by = MagicMock(return_value=flight_search)

        handler = GetFlightSearchesByParametersQueryHandler(repository)
        result = handler.get_by_unsubscribe_code(unsubscribe_code)
        repository.find_one_by.assert_called_once_with({'unsubscribe_code': unsubscribe_code})
        self.assertEqual(result, flight_search)