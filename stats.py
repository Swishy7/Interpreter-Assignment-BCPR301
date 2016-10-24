'''
Created on 24/10/2016

@author: Andrew
'''
from abc import ABCMeta, abstractmethod


class Stats():

    @abstractmethod
    def min(self):
        raise NotImplementedError

    @abstractmethod
    def average(self):
        raise NotImplementedError

    @abstractmethod
    def max(self):
        raise NotImplementedError
