'''
Created on 24/10/2016

@author: Andrew
'''
from abc import ABCMeta, abstractmethod


class StatisticCalculator():

    @abstractmethod
    def build_product(self, type):
        pass

    def calc_min(self, numbers):
        stats_calc = self.build_product(type)
        return stats_calc.min()

    def calc_average(self, numbers):
        stats_calc = self.build_product(type)
        return stats_calc.average()

    def calc_max(self, numbers):
        stats_calc = self.build_product(type)
        return stats_calc.max()
