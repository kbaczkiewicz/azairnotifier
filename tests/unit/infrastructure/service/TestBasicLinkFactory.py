import datetime
import unittest

from tests.data_provider import provide
from azairnotifier.application.value import Parameters
from azairnotifier.infrastructure.service.azair.azairclient import BasicLinkFactory


def mock_data():
    return [(
        Parameters.from_dict(**{
            'airport_from': 'Katowice [KTW]',
            'airport_to': 'Malmo [MMX]',
            'date_from': datetime.datetime(2024, 1, 1),
            'date_to': datetime.datetime(2025, 1, 1),
            'adult_passengers': 1,
            'child_passengers': 0,
            'infant_passengers': 0,
            'min_days': 3,
            'max_days': 5,
            'max_changes': 0,
            'max_price': 300.0
        }),
        'https://www.azair.com/azfin.php?searchtype=flexi&tp=0&isOneway=return&srcAirport=Katowice+%5BKTW%5D&dstAirport=Malmo+%5BMMX%5D&depdate=2024-01-01&arrdate=2025-01-01&minDaysStay=3&maxDaysStay=5&samedep=true&samearr=true&autoprice=true&adults=1&children=0&infants=0&maxChng=0&currency=PLN&lang=en'
    )]

class TestBasicLinkFactory(unittest.TestCase):
    @provide(mock_data())
    def test_it_creates_correct_links(self, params: Parameters, url: str):
        link_factory = BasicLinkFactory()
        self.assertEqual(url, link_factory.create_link(**params.__dict__))



