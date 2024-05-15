import datetime
from typing import Any

from bson import ObjectId
from azairnotifier.application.repository import FlightSearchRepository as FlightSearchRepositoryInterface
from azairnotifier.application.value import FlightSearch
from azairnotifier.config.database.connection import Connection


class FlightSearchRepository(FlightSearchRepositoryInterface):
    __COLLECTION_NAME = 'FlightSearch'

    def __init__(self, mongo_connection: Connection):
        self.collection = mongo_connection.get_collection(self.__COLLECTION_NAME)

    def get(self, pk: str) -> FlightSearch:
        values = self.collection.find_one({'_id': ObjectId(pk)})

        return FlightSearch.from_dict(values) if values else None

    def find_one_by(self, fields: dict[str, Any]) -> FlightSearch:
        values = self.collection.find_one(fields)

        return FlightSearch.from_dict(values) if values else None

    def find_before_date(self, date: datetime.datetime) -> list[FlightSearch]:
        query = {'next_search': {'$lte': date}}

        entities = self.collection.find(query)

        return [FlightSearch.from_dict(entity) for entity in entities]

    def save(self, flight_search: FlightSearch) -> str:
        return self.collection.insert_one(flight_search.model_dump()).inserted_id.__str__()

    def update(self, pk: str, flight_search: FlightSearch) -> None:
        self.collection.update_one(
            {"_id": ObjectId(pk)},
            {"$set": flight_search.model_dump()},
            upsert=True)

    def delete(self, unsubscribe_code: str) -> None:
        self.collection.delete_one({'unsubscribe_code': unsubscribe_code})
