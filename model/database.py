"""Docstring for database"""
from pymongo import MongoClient, errors
from singleton import SingletonMeta

CONNECTION_STRING = "mongodb://root:example@mongodb:27017/form-questions"

class Database(metaclass=SingletonMeta):
    """Docstring for Database"""
    def __init__(self)  -> None:
        self.con_str = CONNECTION_STRING
        try:
            self.client = MongoClient(self.con_str, serverSelectionTimeoutMS=3000)
        except errors.ServerSelectionTimeoutError as err:
            print(err)
            self.client = None

    def __get_database(self):
        """Docstring for __get_database"""
        return self.client['form-questions']

    def update(self, email: str, res: int) -> None:
        """Docstring for update"""
        self.__get_database()['user-form-question'].update_one(
          {'email' : email }, {'$inc': {'result': res}}
        )

    def create(self, data) -> None:
        """Docstring for create"""
        self.__get_database()['user-form-question'].insert_one(data)

    def search(self):
        """Docstring for search"""
        item_details = self.__get_database()['user-form-question'].find()
        for item in item_details:
            print(item)
