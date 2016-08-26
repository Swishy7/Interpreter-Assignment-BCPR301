'''
Created on 21/08/2016

@author: AndrewM
'''

class StatisticCalculator:
    """
        Generates price statistics
    """
        
    def calc_min_price(self, currency_list):
        prices = self.price_translator(currency_list)        
        return min(prices)
        
    
    def calc_max_price(self, currency_list):
        prices = self.price_translator(currency_list)
        return max(prices)
    
    def calc_average_price(self, currency_list):
        prices = self.price_translator(currency_list)
        total = 0;
        for price in prices:
            total += price
        average = total / len(prices)
        return average
    
    # returns a list of prices, used to combine dollar and cent ints to a single float
    def price_translator(self, currency_list):
        price_list = []
        for i in range(len(currency_list)):
            # cut off the $ symbol.
            currency = float(currency_list[i][1:])
            price_list.append(currency)
        return price_list

    def calc_min_views(self, views):
        return min(views)
    
    def calc_max_views(self, views):
        return max(views)
    
    def calc_average_views(self, views):
        total = 0;
        for view in views:
            total += view
        average = total / len(views)
        return average