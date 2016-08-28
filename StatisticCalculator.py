"""
Test the correct views

>>> s = StatisticCalculator()
>>> s.calc_min_views({20, 200, 487, 35})
20
>>> s.calc_max_views({500, 12, 1337, 13})
1337
>>> s.calc_average_views({20, 21, 22})
21.0
"""


class StatisticCalculator:
    """
        Generates price and view statistics
    """

    def calc_min_price(self, currency_list):
        prices = self.price_translator(currency_list)
        return min(prices)

    def calc_max_price(self, currency_list):
        prices = self.price_translator(currency_list)
        return max(prices)

    def calc_average_price(self, currency_list):
        prices = self.price_translator(currency_list)
        total = 0
        for price in prices:
            total += price
        average = total / len(prices)
        return average

    # returns a list of prices, used to combine
    # dollar and cent ints to a single float
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
        total = 0
        for view in views:
            total += view
        average = total / len(views)
        return average

if __name__ == "__main__":
    import doctest
    doctest.testmod()
