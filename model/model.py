"""Docstring for model"""
import pickle

from singleton import SingletonMeta

class Model(metaclass=SingletonMeta):
    """Docstring for model"""
    def __init__(self) -> None:
        with open('model.sav', 'rb') as file:
            self.__model = pickle.load(file)

    def make_prediction(self, data: list) -> int:
        """Docstring for model"""
        return self.__model.predict(data)[0]

    def fun1(self):
        """Docstring for model"""
