'''
Created on 24/10/2016

@author: Andrew
'''
from InterpreterAssignment import stats


class StatsCurrency(stats.Stats):

    def min(self, numbers):
        prices = self.price_translator(numbers)
        return min(prices)

    def average(self, numbers):
        prices = self.price_translator(numbers)
        total = 0
        for price in prices:
            total += price
        average = total / len(prices)
        return average

    def max(self, numbers):
        prices = self.price_translator(numbers)
        return max(prices)

    # returns a list of prices, used to combine
    # dollar and cent ints to a single float
    def price_translator(self, currency_list):
        price_list = []
        for i in range(len(currency_list)):
            # cut off the $ symbol.
            currency = float(currency_list[i][1:])
            price_list.append(currency)
        return price_list
