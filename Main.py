'''
Created on 19/08/2016

@author: AndrewM
'''
from InterpreterAssignment import Controller
from InterpreterAssignment import Product
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import CommandIntepreter
from InterpreterAssignment import FileHandler
def main():
    my_controller = Controller.Controller(HTMLParser.Scrapper(),
                                          CommandIntepreter.CommandIntepreter(),
                                          FileHandler.FileHandler()
                                          )
    my_controller.go()
if __name__ == '__main__':
    main()