import os
from os.path import dirname
from dependency_injector import containers, providers
from azairnotifier.application.service.mailing import Mailer
from azairnotifier.infrastructure.handler.commandhandler import \
    CreateFlightSearchHandler, \
    UpdateFlightSearchHandler, \
    DeleteFlightSearchHandler
from azairnotifier.infrastructure.provider import JsonFileAirportsProvider
from azairnotifier.infrastructure.repository import FlightSearchRepository
from azairnotifier.infrastructure.service.azair.azairclient import \
    BasicLinkFactory, \
    SinglePriceAZAirScraper, \
    AZairClient
from azairnotifier.config.database.connection import Connection
from azairnotifier.infrastructure.handler.queryhandler import \
    GetFlightSearchesQueryHandler, \
    GetFlightSearchesByParametersQueryHandler, GetFlightSearchesBeforeGivenDateQueryHandler


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(auto_wire=False)
    mongo_connection = providers.Singleton(
        Connection,
        database_url=os.environ['DATABASE_URL'],
        database_name=os.environ['DATABASE_NAME']
    )

    flight_search_repository = providers.Factory(
        FlightSearchRepository,
        mongo_connection=mongo_connection
    )

    create_flight_search_handler = providers.Factory(
        CreateFlightSearchHandler,
        repository=flight_search_repository
    )

    update_flight_search_handler = providers.Factory(
        UpdateFlightSearchHandler,
        repository=flight_search_repository
    )

    delete_flight_search_handler = providers.Factory(
        DeleteFlightSearchHandler,
        repository=flight_search_repository
    )

    get_flight_searches_query_handler = providers.Factory(
        GetFlightSearchesQueryHandler,
        repository=flight_search_repository
    )

    get_flight_searches_by_parameters_query_handler = providers.Factory(
        GetFlightSearchesByParametersQueryHandler,
        repository=flight_search_repository
    )

    get_flight_searches_before_date_query_handler = providers.Factory(
        GetFlightSearchesBeforeGivenDateQueryHandler,
        repository=flight_search_repository
    )

    airports_provider = providers.Factory(
        JsonFileAirportsProvider,
        path=dirname(__file__) + "/../resources/airports.json"
    )

    azair_link_factory = providers.Factory(BasicLinkFactory)
    azair_scraper = providers.Factory(SinglePriceAZAirScraper)
    azair_client = providers.Factory(
        AZairClient,
        link_factory=azair_link_factory,
        azair_scraper=azair_scraper
    )

    mailer = providers.Factory(
        Mailer,
        smtp_server=os.environ['MAILING_SMTP_SERVER'],
        port=int(os.environ['MAILING_PORT']),
        sender_email=os.environ['MAILING_SENDER_NAME'],
        sender_password=os.environ['MAILING_PASSKEY']
    )

