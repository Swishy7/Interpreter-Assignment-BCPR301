import unittest
import Controller
import HTMLParser
import CommandIntepreter as CMDI
import FileHandler
import StatisticCalculator as Calc
import coverage

test = coverage.summary
print(test)

class UnitTester(unittest.TestCase):

    def setUp(self):
        self.my_controller = Controller.Controller(
                                            HTMLParser.Scrapper(),
                                            CMDI.CommandIntepreter(),
                                            FileHandler.FileHandler(),
                                            Calc.StatisticCalculator()
                                        )
        self.my_controller.scrape_data()

    def tearDown(self):
        pass

    # test that the scraper will collect the expected amount of items
    # on a page (20)
    def test_product_length(self):
        self.assertEqual(len(self.my_controller.products), 20, "Onoes")

    def test_links_length(self):
        self.assertEqual(len(
                        self.my_controller.my_html_parser.data["links"]),
                        20,
                        "Onoes"
                        )

    def test_descriptions_length(self):
        self.assertEqual(len(
                         self.my_controller.my_html_parser.data
                         ["descriptions"]),
                         20, "Onoes")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
