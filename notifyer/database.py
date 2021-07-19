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
            self.__client = MongoClient(
                host = [ str(domain) + ":" + str(port) ],
                serverSelectionTimeoutMS = 3000, 
                username = username,
                password = password,
            )

        except errors.ServerSelectionTimeoutError as err:
            self.__client = None

            print ("py-mongo ERROR:", err)

    

