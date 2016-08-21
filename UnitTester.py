'''
Created on 21/08/2016

@author: AndrewM
'''
import unittest
from InterpreterAssignment import Controller
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import CommandIntepreter
from InterpreterAssignment import FileHandler

class UnitTester(unittest.TestCase):

    def setUp(self):
        self.my_controller = Controller.Controller(HTMLParser.Scrapper(),
                                          CommandIntepreter.CommandIntepreter(),
                                          FileHandler.FileHandler()
                                          )
        self.my_controller.scrape_data()
        


    def tearDown(self):
        pass

    # test that the scraper will collect the expected amount of items
    # on a page (20)
    def test_product_length(self):
        self.assertEqual(len(self.my_controller.products), 20, "Onoes")
    
    def test_links_length(self):
        self.assertEqual(len(self.my_controller.my_html_parser.data["links"]), 20, "Onoes")
    
    def test_descriptions_length(self):
        self.assertEqual(len(self.my_controller.my_html_parser.data["descriptions"]), 20, "Onoes")
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
