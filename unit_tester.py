import unittest
import controller
import html_parser
import command_interpreter as cmdi
import file_handler
import statistic_calculator_a as calc


class UnitTester(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(UnitTester, cls).setUpClass()
        cls.my_controller = controller.Controller(
                                            html_parser.Scrapper(),
                                            cmdi.CommandInterpreter(),
                                            file_handler.FileHandler(),
                                            calc.StatisticCalculatorA()
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

    def test_no_duplicate_description(self):
        before = len(self.my_controller.products)
        self.my_controller.save_data()
        self.my_controller.load_data()
        after = len(self.my_controller.products)
        self.assertEqual(before, after, "onoes")

    def test_add_product(self):
        self.my_controller.save_data()
        del self.my_controller.products[0]
        before = len(self.my_controller.products)
        self.my_controller.load_data()
        after = len(self.my_controller.products)
        self.assertEqual(before + 1, after, "onoes")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
