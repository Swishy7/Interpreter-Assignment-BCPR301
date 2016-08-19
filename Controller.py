'''
Created on 19/08/2016

@author: AndrewM
'''
from InterpreterAssignment import HTMLParser
from InterpreterAssignment import Product

class Controller:
    '''
    classdocs
    '''
    # instances of Product
    products = []
    
    def __init__(self, the_html_parser, the_command_interpreter):
        '''
        Constructor
        '''
        self.my_html_parser = the_html_parser
        # self.my_product = the_product
        self.my_command_intepreter = the_command_interpreter
        
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
        for i in range(len(self.products)):
            print(self.products[i].get_description())
            print(self.products[i].get_price())
            
            
        # print(web_data)
    def say(self, message):
        print(message)