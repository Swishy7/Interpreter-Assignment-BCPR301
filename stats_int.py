'''
Created on 24/10/2016

@author: Andrew
'''
from InterpreterAssignment import stats


class StatsInt(stats.Stats):

    def min(self, numbers):
        return min(numbers)

    def average(self, numbers):
        total = 0
        for number in numbers:
            total += number
        average = total / len(numbers)
        return average

    def max(self, numbers):
        return max(numbers)
