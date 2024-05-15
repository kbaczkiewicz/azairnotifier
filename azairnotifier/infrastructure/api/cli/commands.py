from datetime import datetime
import typer
from azairnotifier.application.service.mailing import Mailer
from azairnotifier.application.handler.queryhandler import GetFlightSearchesBeforeGivenDateQueryHandler
from azairnotifier.config.di.container import Container
from azairnotifier.infrastructure.service.azair.azairclient import AZairClient

app = typer.Typer()


@app.command()
def mailing():
    query_handler: GetFlightSearchesBeforeGivenDateQueryHandler = Container.get_flight_searches_before_date_query_handler()
    mailer: Mailer = Container.mailer()
    azair_client: AZairClient = Container.azair_client()

    for flight_searches in query_handler.get(datetime.now()):
        for parameters in flight_searches.parameters:
            pass