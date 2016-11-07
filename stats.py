'''
Created on 24/10/2016

@author: Andrew
'''
from abc import ABCMeta, abstractmethod


class Stats(metaclass=ABCMeta):

    @abstractmethod
    def min(self, numbers):
        raise NotImplementedError

    @abstractmethod
    def average(self, numbers):
        raise NotImplementedError

    @abstractmethod
    def max(self, numbers):
        raise NotImplementedError
