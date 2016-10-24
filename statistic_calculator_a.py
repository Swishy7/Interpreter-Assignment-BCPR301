"""
Test the correct views

>>> s = StatisticCalculatorA()
>>> s.calc_min_views({20, 200, 487, 35})
20
>>> s.calc_max_views({500, 12, 1337, 13})
1337
>>> s.calc_average_views({20, 21, 22})
21.0
"""
from InterpreterAssignment import statistic_calculator as stat_calc
from InterpreterAssignment import stats_int
from InterpreterAssignment import stats_currency

class StatisticCalculatorA(stat_calc.StatisticCalculator):
    """
        Generates price and view statistics
    """
    def build_product(self, numbers):
        if(type(numbers[0]) is int):
            return stats_int.StatsInt()
        elif(type(numbers[0]) is str):
            return stats_currency.StatsCurrency()
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
