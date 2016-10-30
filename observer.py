'''
Created on 30/10/2016

@author: Andrew
'''
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    def __init__(self):
        self.product_count = 0
        self.subject = None

    @abstractmethod
    def update(self, product_count):
        pass

    def set_subject(self, new_subject):
        self.subject = new_subject
