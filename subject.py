'''
Created on 30/10/2016

@author: Andrew
'''
from abc import ABCMeta


class Subject(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()