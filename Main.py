"""
Created on 19/08/2016

@author: AndrewM
"""
import Controller
import HTMLParser
import CommandIntepreter as CMDI
import FileHandler
import StatisticCalculator as Calc
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
