"""
Test the stuffs

>>> f = FileHandler()
>>> f.set_path("C:")
>>> f.get_db_path()
'C:\\\\'
"""
import pickle
import os


class FileHandler:
    """
    classdocs
    """
    path = ""
    products = []
    file_name = "database"

    def __init__(self):
        '''
        Constructor
        '''

    def set_path(self, the_path):
        # add a \ to the path, should the user forget to do so
        if the_path[-1:] != "\\":
            the_path += "\\"
        if self.verify_path(the_path):
            self.path = the_path
        else:
            print("Invalid Path")

    def get_db_path(self):
        return self.path

    # put a try / except on path reading, because it might not exist :P
    # or have a function to verify paths before hand.

    def write_database(self, the_product):
        self.products = the_product
        with open(self.path + self.file_name + '.pickle', 'wb') as handle:
            pickle.dump(self.products, handle)

    def read_database(self):
        # if no path is given, the file will be saved in Python directory
        try:
            with open(self.path + self.file_name + '.pickle', 'rb') as handle:
                loaded_products = pickle.load(handle)
                return loaded_products
        except FileNotFoundError:
            print("File not found (> >.< <) " +
                  "Try another path, or setting the file name")

    def verify_path(self, the_path):
        # testing path requires forward slash not back.
        formatted_path = the_path.replace("\\", "/")
        # detects whether the path is
        return os.path.isdir(formatted_path)

    def set_file_name(self, the_file_name):
        self.file_name = the_file_name

if __name__ == "__main__":
    import doctest
    doctest.testmod()
