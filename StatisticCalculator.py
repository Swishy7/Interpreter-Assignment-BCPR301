'''
Created on 21/08/2016

@author: AndrewM
'''

class StatisticCalculator:
    """
    classdocs
    """


    def __init__(self, params):
        '''
        Constructor
        '''
        
    # will have to concatenate the integers with the decimals
    # to form a float, then will have to
    # put them in a list, and then compare
    # and then return the string
        
    def calc_min(self, dollars_list, cents_list):
        prices = self.price_translator(dollars_list, cents_list)        
        return min(prices)
        
    
    def calc_max(self, dollars_list, cents_list):
        prices = self.price_translator(dollars_list, cents_list)
        return max(prices)
    
    def calc_average(self, dollars_list, cents_list):
        prices = self.price_translator(dollars_list, cents_list)
        total = 0;
        for price in prices:
            total += price
        average = total / len(prices)
        return average
      
    def price_translator(self, dollars_list, cents_list):
        price_list = []
        for i in range(len(dollars_list)):
            currency = float(dollars_list[i] + "0." + cents_list[i])
            price_list.append(currency)
        print(price_list)
        return price_list
        

#    old code
#             dollars = int(price[1:].rsplit('.', 1)[0])
#             cents = int("0." + price[len(str(dollars))+2:].rsplit('+', 1)[0])
#             currency = dollars + cents
            #price_list.append(currency)

    
    