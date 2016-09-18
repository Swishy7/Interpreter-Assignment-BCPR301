"""
Created on 19/08/2016

@author: AndrewM
"""
import controller
import html_parser
import command_interpreter as cmdi
import file_handler
import statistic_calculator as calc
import sys


def main():
    my_controller = controller.Controller(html_parser.Scrapper(),
                                          cmdi.CommandInterpreter(),
                                          file_handler.FileHandler(),
                                          calc.StatisticCalculator()
                                          )
    auto_run_scraper = False
    if len(sys.argv) > 1 and sys.argv[1] == 'true':
        auto_run_scraper = True
    my_controller.go(auto_run_scraper)
if __name__ == '__main__':
    main()
