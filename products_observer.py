'''
Created on 30/10/2016

@author: Andrew
'''
from InterpreterAssignment.observer import Observer


class ProductObserver(Observer):
    def __init__(self):
        self.product_count = 0

    def update(self):
        self.product_count = len(self.subject.products)
        print("(> ^_^ )>---[ " +
              str(self.product_count) + " products are loaded. ]")
