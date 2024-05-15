from pymongo import MongoClient


class Connection:
    def __init__(self, database_url: str, database_name: str):
        self.__database = MongoClient(database_url)[database_name]

    def get_collection(self, collection_name: str):
        return self.__database[collection_name]
