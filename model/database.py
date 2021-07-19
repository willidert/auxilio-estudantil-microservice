from pymongo import MongoClient, errors
from singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    def __init__(self, CONNECTION_STRING="mongodb://root:example@mongodb:27017/form-questions") -> None:
        self.CONNECTION_STRING=CONNECTION_STRING
        try:
            self.client = MongoClient(self.CONNECTION_STRING, serverSelectionTimeoutMS=3000)
        except errors.serverSelectionTimeoutError as err:
            print(err)
            self.client = None
    
    def __get_database(self):
        return self.client['form-questions']
    
    def update(self, email: str, res: int) -> None:
        result = self.__get_database()['user-form-question'].update_one({'email' : email }, {'$inc': {'result': res}})
    
    def create(self, data) -> None:
        self.__get_database()['user-form-question'].insert_one(data)

    def search(self):
        item_details = self.__get_database()['user-form-question'].find()
        for item in item_details:
            print(item)
