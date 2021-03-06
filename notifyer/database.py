from pymongo import MongoClient, errors


class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def __call__(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance


@Singleton
class DataBaseConnection(object):

    def __init__(self, domain='mongodb', port='27017', username='root', password="example"):

        try:
            self.__client = MongoClient(f"mongodb://{username}:{password}@{domain}:{port}/{database_name}",
                                        serverSelectionTimeoutMS=timeout,
                                        )

        except errors.ServerSelectionTimeoutError as err:
            self.__client = None

            print("py-mongo ERROR:", err)

    def __get_database(self):
        return self.__client['form-questions']

    def update(self, email, result: int) -> None:
        self.__get_database()['user-form-question'].update_one(
            {'email': email}, {'$inc': {'email-sended': result}})
