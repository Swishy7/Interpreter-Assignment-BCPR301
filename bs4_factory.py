'''
Created on 30/10/2016

@author: Andrew
'''


class BS4Factory():

    def __init__(self, params):
        self.__flyweight_pool = {}
        
    def get_flyweight(self, key):
        if key not in self.__flyweight_pool:
            self.__flyweight_pool[key] = eval(key + "()")
        return self.__flyweight_pool[key]
