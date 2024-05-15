import random
from datetime import datetime

from azairnotifier.application.command import DeleteFlightSearchCommand, UpdateFlightSearchCommand, \
    CreateFlightSearchCommand, ProcessMailingCommand
from azairnotifier.application.handler.commandhandler import \
    CreateFlightSearchHandler as CreateFlightSearchHandlerInterface, \
    UpdateFlightSearchHandler as UpdateFlightSearchHandlerInterface, \
    DeleteFlightSearchHandler as DeleteFlightSearchHandlerInterface, \
    ProcessMailingCommandHandler as ProcessMailingCommandHandlerInterface
from azairnotifier.application.repository import FlightSearchRepository
from azairnotifier.application.value import FlightSearch
from azairnotifier.application.factory import ParametersFactory


class CreateFlightSearchHandler(CreateFlightSearchHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        self.repository = repository

    def handle(self, command: CreateFlightSearchCommand) -> str:
        params = ParametersFactory.from_command(command)
        flight_search = FlightSearch(
            email=command.email,
            next_search=datetime.now(),
            parameters=[params.model_dump()],
            unsubscribe_code='%032x' % random.getrandbits(128)
        )

        return str(self.repository.save(flight_search))


class UpdateFlightSearchHandler(UpdateFlightSearchHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        self.repository = repository

    def handle(self, command: UpdateFlightSearchCommand) -> None:
        params = ParametersFactory.from_command(command)
        entity = self.repository.get(command.pk)
        entity.parameters.append(params.model_dump())

        self.repository.update(command.pk, entity)


class DeleteFlightSearchHandler(DeleteFlightSearchHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        self.repository = repository

    def handle(self, command: DeleteFlightSearchCommand) -> None:
        self.repository.delete(command.code)


class ProcessMailingCommandHandler(ProcessMailingCommandHandlerInterface):
    def __init__(self, repository: FlightSearchRepository):
        pass

    def handle(self, command: ProcessMailingCommand) -> None:
        pass
