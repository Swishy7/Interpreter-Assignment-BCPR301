import Product


class Controller:
    """
    classdocs

    """
    products = []

    def __init__(self,
                 the_html_parser,
                 the_command_interpreter,
                 the_file_handler,
                 the_statistics_calculator):
        '''
        Constructor
        '''
        self.my_html_parser = the_html_parser
        # self.my_product = the_product
        self.my_command_intepreter = the_command_interpreter
        self.my_file_handler = the_file_handler
        self.my_statistic_calculator = the_statistics_calculator

    def go(self, is_auto_scrape):
        if is_auto_scrape:
            self.scrape_data()
        self.my_command_intepreter.set_controller(self)
        # start the CMD here.
        self.my_command_intepreter.cmdloop()

    # Called by CommandInterpreter.
    def save_data(self):
        # save the products to the database, if they exist
        if len(self.products) > 0:
            self.my_file_handler.write_database(self.products)
        else:
            print("There are no products to save")
    # add unique

    def load_data(self):
        # save existing descriptions in a list, so that they can be compared
        # with loaded descriptions to determine if they already exist.
        descriptions = []
        self.get_descriptions(descriptions)
        # for every instance of product saved,
        # load it, get it's object data, then store it.
        loaded_data = self.my_file_handler.read_database()
        if loaded_data is not None:
            for loaded_product in loaded_data:
                # if the description is not found,
                # it's not in the list, add it.
                if loaded_product.get_description() not in descriptions:
                    self.products.append(loaded_product)
            print("Loaded " + str(len(self.products)) + " products")

    def set_db_path(self, the_path):
        self.my_file_handler.set_path(the_path)

    def get_db_path(self):
        print(self.my_file_handler.get_db_path())

    def scrape_data(self):
        self.my_html_parser.collect_data()
        web_data = self.my_html_parser.get_data()
        date = web_data["date"]
        # used to verify repeat descriptions are not being added.
        descriptions = []
        # if there are existing products, add the descriptions to list.
        # (> ^_^ )>---[ convert the next 3 lines to a function ]
        if len(self.products) > 0:
            self.get_descriptions(descriptions)
        # sort through the scrapped data and
        for i in range(len(web_data["descriptions"])):
            # if the description isn't already saved, save it.
            if web_data["descriptions"][i] not in descriptions:
                self.add_product(web_data["descriptions"][i],
                                 web_data["prices"][i],
                                 web_data["links"][i],
                                 web_data["views"][i],
                                 date)

    # checks an object to see if it contains anything
    # checks the products if nothing is passed in

    def get_descriptions(self, descriptions):
        for product in self.products:
            descriptions.append(product.get_description())

    def add_product(self, description, price, link, view, date):
        self.products.append(Product.Product(description,
                                             price[0],
                                             price[1],
                                             link,
                                             date,
                                             view))

    def check_data(self, data=products):
        if len(data) > 0:
            return True
        else:
            return False

    def display_data(self):
        if self.check_data():
            for product in self.products:
                print(product.get_object())
        else:
            print("No products to display try loading or scraping")

    def get_average_price(self):
        if self.check_data():
            currency = self.get_currency()
            print("{0:.2f}".format(
                            self.my_statistic_calculator.calc_average_price(
                                                                    currency)))
        else:
            print("No products to display try loading or scraping")

    def get_max_price(self):
        if self.check_data():
            currency = self.get_currency()
            print(self.my_statistic_calculator.calc_max_price(currency))
        else:
            print("No products to display try loading or scraping")

    def get_min_price(self):
        if self.check_data():
            currency = self.get_currency()
            print(self.my_statistic_calculator.calc_min_price(currency))

    # returns a list of currencies from the loaded products
    def get_currency(self):
        currency = []
        for product in self.products:
            currency.append(product.get_price())
        return currency

    def get_views(self):
        views = []
        for product in self.products:
            views.append(product.get_views())
        return views

    def get_min_views(self):
        if self.check_data():
            views = self.get_views()
            print(self.my_statistic_calculator.calc_min_views(views))
        else:
            print("No products to display try loading or scraping")

    def get_max_views(self):
        if self.check_data():
            views = self.get_views()
            print(self.my_statistic_calculator.calc_max_views(views))
        else:
            print("No products to display try loading or scraping")

    def get_average_views(self):
        if self.check_data():
            views = self.get_views()
            print(self.my_statistic_calculator.calc_average_views(views))
        else:
            print("No products to display try loading or scraping")

    def set_file_name(self, name):
        self.my_file_handler.set_file_name(name)
