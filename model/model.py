import pickle

from singleton import SingletonMeta

class Model(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.__model = pickle.load(open('model.sav', 'rb'))

    def make_prediction(self, data: list) -> int:
        return self.__model.predict(data)[0]
