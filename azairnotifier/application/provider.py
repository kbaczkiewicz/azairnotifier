import abc


class AirportsProvider(abc.ABC):
    @abc.abstractmethod
    def get_airports(self) -> dict:
        pass
