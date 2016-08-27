"""
Created on 19/08/2016

@author: AndrewM
"""
from InterpreterAssignment import Controller
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import CommandIntepreter as CMDI
from InterpreterAssignment import FileHandler
from InterpreterAssignment import StatisticCalculator as Calc


def main():
    my_controller = Controller.Controller(HTMLParser.Scrapper(),
                                          CMDI.CommandIntepreter(),
                                          FileHandler.FileHandler(),
                                          Calc.StatisticCalculator()
                                          )
    my_controller.go()
if __name__ == '__main__':
    main()
