'''
Created on 19/08/2016

@author: AndrewM
'''

class Product:
    '''
    classdocs
    '''
    

    def __init__(self, the_description, the_dollars, the_cents, the_link, the_date):
        '''
        Constructor (> ^_^ )>
        '''
        self.description = the_description
        self.dollars = the_dollars
        self.cents = the_cents
        self.link = the_link
        self.date = the_date
        
    def get_description(self):
        return self.description
    
    def get_dollars(self):
        return self.dollars
    
    def get_cents(self):
        return self.cents
    
    def get_price(self):
        return "$" + str(self.dollars) + "." + str(self.cents)
    
    def get_link(self):
        return self.link
    
    def get_date(self):
        return self.date
    
    def get_object(self):
        return {"description": self.description,
                "dollars": self.dollars,
                "cents": self.cents,
                "link": self.link,
                "date": self.date
                }
    
    
        