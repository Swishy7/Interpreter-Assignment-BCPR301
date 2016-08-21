'''
Created on 19/08/2016

@author: AndrewM
'''
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import Product
from InterpreterAssignment import FileHandler

class Controller:
    '''
    classdocs
    '''
    # instances of Product
    #products = set()
    products = []
    # object counterparts of product
    #product_object = frozenset()
    
    def __init__(self, the_html_parser, the_command_interpreter, the_file_handler):
        '''
        Constructor
        '''
        self.my_html_parser = the_html_parser
        # self.my_product = the_product
        self.my_command_intepreter = the_command_interpreter
        self.my_file_handler = the_file_handler
        
    def go(self):
        self.my_command_intepreter.set_controller(self)
        self.my_html_parser.collect_data()
        web_data = self.my_html_parser.get_data()
        date = web_data["date"]
        for i in range(len(web_data["descriptions"])):
            desc = web_data["descriptions"][i]
            price = web_data["prices"][i]
            link = web_data["links"][i]
            self.products.append(Product.Product(desc,price[0],price[1],link,date))
            # print("Dollars: " + str(price[0]) + " Cents " + str(price[1]))
        # start the CMD here, no more code will run until exiting.
        self.my_command_intepreter.cmdloop()
        # TESTING, NEED SOME TYPE OF VIEW FOR PRINTING
#         for i in range(len(self.products)):
#             print(self.products[i].get_description())
#             print(self.products[i].get_price())

    # Called by CommandInterpreter. 
    def save_data(self):
        # save the products to the database, if they exist
        if len(self.products) > 0:
            #objects = []
            #for product in self.products:
                #objects.append(product.get_object())
                #print(objects)
            self.my_file_handler.write_database(self.products)
        else:
            print("There are no products to save")
    # add unique 
    def load_data(self):
        # save existing descriptions in a list, so that they can be compared with
        # loaded descriptions to determine if they already exist.
        descriptions = []
        for product in self.products:
            descriptions.append(product.get_description())
        # for every instance of product saved, load it, get it's object data, then store it.
        for loaded_product in self.my_file_handler.read_database():
            # if the description is not found, it's not in the list, add it.
            if loaded_product.get_description() not in descriptions:
                self.products.append(loaded_product.get_object())
        print(str(len(self.products)))
        
    def set_db_path(self, the_path):
        self.my_file_handler.set_path(the_path)
        
    def get_db_path(self):
        print(self.my_file_handler.get_db_path())
        