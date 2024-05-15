import datetime
from typing import Any, Unpack

from pydantic import BaseModel, ConfigDict


class FlightSearch(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    email: str
    next_search: datetime.datetime
    parameters: list["Parameters"]
    unsubscribe_code: str

    @classmethod
    def from_dict(cls, values: dict[str, Any]):
        return FlightSearch(
            email=values['email'],
            next_search=values['next_search'],
            parameters=Parameters.from_dict(**values['parameters']),
            unsubscribe_code=values['unsubscribe_code']
        )


class Parameters(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    airport_from: str
    airport_to: str
    date_from: datetime
    date_to: datetime
    adult_passengers: int
    child_passengers: int
    infant_passengers: int
    min_days: int
    max_days: int
    max_changes: int
    max_price: float

    @classmethod
    def from_dict(cls, **kwargs: Unpack['Parameters']) -> 'Parameters':
        return Parameters(
            airport_from=kwargs['airport_from'],
            airport_to=kwargs['airport_to'],
            date_from=kwargs['date_from'],
            date_to=kwargs['date_to'],
            adult_passengers=kwargs['adult_passengers'],
            child_passengers=kwargs['child_passengers'],
            infant_passengers=kwargs['infant_passengers'],
            min_days=kwargs['min_days'],
            max_days=kwargs['max_days'],
            max_changes=kwargs['max_changes'],
            max_price=kwargs['max_price']
        )