"""
Created on 19/08/2016

@author: AndrewM
"""
from InterpreterAssignment import Controller
from InterpreterAssignment import Product
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import CommandIntepreter
from InterpreterAssignment import FileHandler
from InterpreterAssignment import StatisticCalculator
def main():
    my_controller = Controller.Controller(HTMLParser.Scrapper(),
                                          CommandIntepreter.CommandIntepreter(),
                                          FileHandler.FileHandler(),
                                          StatisticCalculator.StatisticCalculator()
                                          )
    my_controller.go()
if __name__ == '__main__':
    main()