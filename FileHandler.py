'''
Created on 20/08/2016

@author: AndrewM
'''
import pickle

class FileHandler:
    '''
    classdocs
    '''
    path = ""
    products = []
    test = [{'description': '[Team Group] Xtreem DDR3 LV 4GB Kit (2x2GB) DDR3-1600 1.65V 7-7-7-21', 'date': '2016-08-20 20:26:59', 'dollars': 165, 'link': 'http://www.impc.co.nz/products/iw_4434.html', 'cents': 72}, {'description': '[Team Group] Xtreem DDR3 LV 8GB Kit (2x4GB) DDR3-2133 1.65V 10-10-10-30', 'date': '2016-08-20 20:26:59', 'dollars': 167, 'link': 'http://www.impc.co.nz/products/iw_1554.html', 'cents': 80}, {'description': '12GB 1600MHz Kit of 3 SR x 8 1.35V w TS', 'date': '2016-08-20 20:26:59', 'dollars': 131, 'link': 'http://www.impc.co.nz/products/im_2565953.html', 'cents': 46}, {'description': '16GB 1333MHz Reg ECC Low Voltage Module', 'date': '2016-08-20 20:26:59', 'dollars': 134, 'link': 'http://www.impc.co.nz/products/im_1931557.html', 'cents': 42}, {'description': '16GB 2Rx4 PC3L-10600R-9 Kit', 'date': '2016-08-20 20:26:59', 'dollars': 515, 'link': 'http://www.impc.co.nz/products/im_1891309.html', 'cents': 51}, {'description': '16GB DDR3 1333MHz Reg ECC LV Module for HP', 'date': '2016-08-20 20:26:59', 'dollars': 135, 'link': 'http://www.impc.co.nz/products/im_1744613.html', 'cents': 84}, {'description': '16GB DDR4-2133MHZ ECC REG', 'date': '2016-08-20 20:26:59', 'dollars': 125, 'link': 'http://www.impc.co.nz/products/im_2779715.html', 'cents': 76}, {'description': '16GB DDR4-2133MHz REG ECC CL 15', 'date': '2016-08-20 20:26:59', 'dollars': 127, 'link': 'http://www.impc.co.nz/products/im_3040839.html', 'cents': 30}, {'description': '16GB DDR4-2400MHz CL15 DIMM', 'date': '2016-08-20 20:26:59', 'dollars': 112, 'link': 'http://www.impc.co.nz/products/im_3238653.html', 'cents': 67}, {'description': '16GB DDR4-2666MHz NON-ECC CL 15', 'date': '2016-08-20 20:26:59', 'dollars': 130, 'link': 'http://www.impc.co.nz/products/im_3007540.html', 'cents': 46}, {'description': '16GB RDIMM 2133 MT/s Dual Rank x4 Dat', 'date': '2016-08-20 20:26:59', 'dollars': 377, 'link': 'http://www.impc.co.nz/products/im_2781121.html', 'cents': 25}, {'description': '1GB DDR400 184PIN DIMM 128MX64 CL3', 'date': '2016-08-20 20:26:59', 'dollars': 58, 'link': 'http://www.impc.co.nz/products/im_1007516.html', 'cents': 35}, {'description': '1GB PC5300 DDR2 SO-DIMM 667MHz', 'date': '2016-08-20 20:26:59', 'dollars': 15, 'link': 'http://www.impc.co.nz/products/im_3022707.html', 'cents': 0}, {'description': '1X16GB PC3-14900 DDR3 1866MHZ 240 PIN', 'date': '2016-08-20 20:26:59', 'dollars': 165, 'link': 'http://www.impc.co.nz/products/im_3054980.html', 'cents': 87}, {'description': '2GB 1333MHz DDR3 Non-ECC CL9 DIMM Single', 'date': '2016-08-20 20:26:59', 'dollars': 18, 'link': 'http://www.impc.co.nz/products/im_2554389.html', 'cents': 49}, {'description': '2GB 1600MHz DDR3 Non-ECC CL11 DIMM Singl', 'date': '2016-08-20 20:26:59', 'dollars': 20, 'link': 'http://www.impc.co.nz/products/im_2554391.html', 'cents': 40}, {'description': '2GB DDR2-800 PC-6400 So-Dimm Mac', 'date': '2016-08-20 20:26:59', 'dollars': 24, 'link': 'http://www.impc.co.nz/products/im_2767834.html', 'cents': 0}, {'description': '2GB x 2 PC8500 DDR3 SODIMM 4GB Kit', 'date': '2016-08-20 20:26:59', 'dollars': 52, 'link': 'http://www.impc.co.nz/products/im_2948594.html', 'cents': 51}, {'description': '32GB 1066MHz Quad Rank Reg ECC Module LV', 'date': '2016-08-20 20:26:59', 'dollars': 900, 'link': 'http://www.impc.co.nz/products/im_2061338.html', 'cents': 52}, {'description': '4GB 2133MHz DDR4 Non-ECC CL15', 'date': '2016-08-20 20:26:59', 'dollars': 28, 'link': 'http://www.impc.co.nz/products/im_2940470.html', 'cents': 68}]
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
    
    def write_database(self, the_product):
        self.products = the_product
        #print("Products passed in: " + str(type(self.products)) + "\n" + "Test data: " + str(type(self.test))
        with open(self.path+'filename.pickle', 'wb') as handle:
             pickle.dump(self.products, handle)
        #print(self.products)
        
    def read_database(self):
        # if no path is given, the file will be saved in Python directory
        with open('filename.pickle', 'rb') as handle:
            loaded_products = pickle.load(handle)
            return loaded_products