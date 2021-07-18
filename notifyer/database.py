from pymongo import MongoClient, errors

class Singleton:

    def __init__(self, cls):
        self.__cls = cls

    def Instance(self):
        try:
            return self.__instance
        except AttributeError:
            self.__instance = self.__cls()
            return self.__instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self.__cls)

@Singleton
class DataBaseConnection(object):

    def __init__(self, domain='mongodb', port='27017', username='root', password="example"):
        self.__domain = domain
        self.__port = port
        self.__username = username
        self.__password = password

        try:
            self.__client = MongoClient(
                host = [ str(self.__domain) + ":" + str(self.__port) ],
                serverSelectionTimeoutMS = 3000, 
                username = self.__username,
                password = self.__password,
            )

        except errors.ServerSelectionTimeoutError as err:
            self.__client = None

            print ("pymongo ERROR:", err)

    def __str__(self):
        return self.__client()


