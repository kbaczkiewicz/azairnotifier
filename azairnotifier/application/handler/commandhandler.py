import abc
from azairnotifier.application.command import CreateFlightSearchCommand, UpdateFlightSearchCommand, \
    DeleteFlightSearchCommand, ProcessMailingCommand


class CreateFlightSearchHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, command: CreateFlightSearchCommand) -> str:
        pass


class UpdateFlightSearchHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, command: UpdateFlightSearchCommand) -> None:
        pass


class DeleteFlightSearchHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, command: DeleteFlightSearchCommand) -> None:
        pass


class ProcessMailingCommandHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, command: ProcessMailingCommand) -> None:
        pass
