"""
Created on 19/08/2016

@author: AndrewM
"""

from InterpreterAssignment import Controller
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import CommandIntepreter as CMDI
from InterpreterAssignment import FileHandler
from InterpreterAssignment import StatisticCalculator as Calc
import sys

def main():
    my_controller = Controller.Controller(HTMLParser.Scrapper(),
                                          CMDI.CommandIntepreter(),
                                          FileHandler.FileHandler(),
                                          Calc.StatisticCalculator()
                                          )
    auto_run_scraper = False
    if len(sys.argv) > 1 and sys.argv[1] == 'true':
        auto_run_scraper = True
    my_controller.go(auto_run_scraper)
if __name__ == '__main__':
    main()
