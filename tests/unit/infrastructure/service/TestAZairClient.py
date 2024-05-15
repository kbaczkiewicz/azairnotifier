import datetime
import unittest
from unittest.mock import patch, MagicMock
from azairnotifier.infrastructure.service.azair.azairclient import AZairClient, LinkFactory, AZairScraper
from azairnotifier.application.value import Parameters
from tests.data_provider import provide


def mock_data():
    return [(
        Parameters.from_dict(**{
            'airport_from': 'KTW',
            'airport_to': 'MMX',
            'date_from': datetime.datetime.now(),
            'date_to': datetime.datetime(2025, 1, 1),
            'adult_passengers': 1,
            'child_passengers': 0,
            'infant_passengers': 0,
            'min_days': 3,
            'max_days': 5,
            'max_changes': 0,
            'max_price': 300.0
        }),
        'https://www.azair.eu/azfin.php?searchtype=flexi&tp=0&isOneway=return&srcAirport=Katowice+%5BKTW%5D&srcFreeAirport=&srcTypedText=katowice&srcFreeTypedText=&srcMC=&dstAirport=Malmo+%5BMMX%5D&dstFreeAirport=&dstTypedText=malm&dstFreeTypedText=&dstMC=&depmonth=202404&depdate=2024-04-29&aid=0&arrmonth=202501&arrdate=2025-01-01&minDaysStay=3&maxDaysStay=5&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&samedep=true&samearr=true&minHourStay=0%3A45&maxHourStay=23%3A20&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&autoprice=true&adults=1&children=0&infants=0&maxChng=0&currency=EUR&lang=en&indexSubmit=Search',
        300.0
    )]

class TestAZairClient(unittest.TestCase):
    @patch('azairnotifier.infrastructure.service.azair.azairclient.AZairScraper')
    @patch('azairnotifier.infrastructure.service.azair.azairclient.LinkFactory')
    @provide(mock_data())
    def test_returns_prices_for_given_parameters(
        self,
        link_factory: LinkFactory,
        azair_scraper: AZairScraper,
        parameters: Parameters,
        url: str,
        price: float
    ):
        link_factory.create_link = MagicMock(return_value=url)
        azair_scraper.scrape_prices = MagicMock(return_value=price)

        client = AZairClient(link_factory, azair_scraper)
        self.assertEqual(price, client.get_prices(parameters))

        link_factory.create_link.assert_called_once_with(**parameters.__dict__)
        azair_scraper.scrape_prices.assert_called_once_with(url)
