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
    products = []
    
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
            for product in self.products:
                self.my_file_handler.write_database(product)
        else:
            print("There are no products to save")
    
    def set_db_path(self, the_path):
        self.my_file_handler.set_path(the_path)
        
    def get_db_path(self):
        print(self.my_file_handler.get_db_path())
        