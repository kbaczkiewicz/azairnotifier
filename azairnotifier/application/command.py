import datetime

from pydantic import BaseModel, ConfigDict


class CreateFlightSearchCommand(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    email: str
    main_source_airport: str
    optional_source_airports: list[str]
    main_dest_airport: str
    optional_dest_airports: list[str]
    max_changes: int
    adults: int
    children: int
    infants: int
    date_from: datetime.datetime
    date_to: datetime.datetime
    min_days: int
    max_days: int
    max_price: float


class UpdateFlightSearchCommand(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    pk: str
    main_source_airport: str
    optional_source_airports: list[str]
    main_dest_airport: str
    optional_dest_airports: list[str]
    max_changes: int
    adults: int
    children: int
    infants: int
    date_from: datetime.datetime
    date_to: datetime.datetime
    min_days: int
    max_days: int
    max_price: float


class DeleteFlightSearchCommand(BaseModel):
    code: str


class ProcessMailingCommand(BaseModel):
    ids: list[str]
