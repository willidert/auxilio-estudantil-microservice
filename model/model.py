import pickle
from singleton import SingletonMeta


class Model(metaclass=SingletonMeta):
    def __init__(self) -> None:
        with open('model.sav', 'rb') as file:
            self.__model = pickle.load(file)

    def make_prediction(self, data: list) -> int:
        return self.__model.predict(data)[0]
