import unittest
import Controller
import HTMLParser
import CommandIntepreter as CMDI
import FileHandler
import StatisticCalculator as Calc
import coverage


class UnitTester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(UnitTester, cls).setUpClass()
        cls.my_controller = Controller.Controller(
                                            HTMLParser.Scrapper(),
                                            CMDI.CommandIntepreter(),
                                            FileHandler.FileHandler(),
                                            Calc.StatisticCalculator()
                                        )
        cls.my_controller.scrape_data()

    def setUp(self):
        pass

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

    def test_product_description(self):
        self.assertEqual(type(
                         self.my_controller.products[0].get_description()
                         ) is str, True, "onoes")

    def test_product_dollars(self):
        self.assertEqual(type(
                         self.my_controller.products[0].get_dollars()
                         ) is int, True, "onoes")

    def test_product_cents(self):
        self.assertEqual(type(
                         self.my_controller.products[0].get_cents()
                         ) is int, True, "onoes")

    def test_product_link(self):
        self.assertEqual(type(
                         self.my_controller.products[0].get_link()
                         ) is str, True, "onoes")

    def test_product_view(self):
        self.assertEqual(type(
                         self.my_controller.products[0].get_views()
                         ) is int, True, "onoes")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
