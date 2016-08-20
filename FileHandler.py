'''
Created on 20/08/2016

@author: AndrewM
'''
import shelve
# the dictionary of dictionaries (product class instances) that shelve will have to store.
product = {}
class FileHandler:
    '''
    classdocs
    '''
    path = ""
    database = None;

    def __init__(self):
        '''
        Constructor
        '''
        
    def set_path(self, the_path):
        # add a / to the path, should the user forget to do so
        if the_path[-1:] != "\\":
            the_path += "\\"
        self.path = the_path
    
    def get_db_path(self):
        return self.path
#     def connect_database(self):
#         # if it does not exist, will create the database.
#         self.database = shelve.open(self.path + 'product.db', writeback=True)
#         self.database.close()
    
    def write_database(self, the_product):
        # if it does not exist, will create the database.
        self.database = shelve.open(self.path + 'product.db', writeback=True)
        self.database["product"] = the_product
    
    