import abc
from urllib.parse import urlencode
import requests
import re
from typing import Unpack, Any, override
from bs4 import BeautifulSoup
from azairnotifier.application.value import Parameters


class LinkFactory(abc.ABC):
    @abc.abstractmethod
    def create_link(self, **kwargs: Any) -> str:
        pass


class AZairScraper(abc.ABC):
    @abc.abstractmethod
    def scrape_prices(self, url: str) -> list[float]:
        pass


class BasicLinkFactory(LinkFactory):
    BASE_URL = 'https://www.azair.com/azfin.php'

    @override
    def create_link(self, **kwargs: Unpack[Parameters]) -> str:
        query_string = urlencode({
            'searchtype': 'flexi',
            'tp': '0',
            'isOneway': 'return',
            'srcAirport': kwargs['airport_from'],
            'dstAirport': kwargs['airport_to'],
            'depdate': kwargs['date_from'].strftime('%Y-%m-%d'),
            'arrdate': kwargs['date_to'].strftime('%Y-%m-%d'),
            'minDaysStay': kwargs['min_days'],
            'maxDaysStay': kwargs['max_days'],
            'samedep': 'true',
            'samearr': 'true',
            'autoprice': 'true',
            'adults': kwargs['adult_passengers'],
            'children': kwargs['child_passengers'],
            'infants': kwargs['infant_passengers'],
            'maxChng': kwargs['max_changes'],
            'currency': 'PLN',
            'lang': 'en'
        })

        return self.BASE_URL + '?' + query_string


class SinglePriceAZAirScraper(AZairScraper):
    @override
    def scrape_prices(self, url: str) -> list[float]:
        content = requests.get(url).content
        soup = BeautifulSoup(content, 'html.parser')
        prices = [float(re.sub("\D", '', i.text)) for i in soup.find_all('span', class_='tp')]

        return [prices[0]]


class AZairClient:
    def __init__(self, link_factory: LinkFactory, azair_scraper: AZairScraper):
        self.link_factory = link_factory
        self.azair_scraper = azair_scraper

    def get_prices(self, parameters: Parameters) -> list[float]:
        return self.azair_scraper.scrape_prices(self._get_link_for_search(parameters))

    def _get_link_for_search(self, parameters: Parameters) -> str:
        return self.link_factory.create_link(**parameters.__dict__)
