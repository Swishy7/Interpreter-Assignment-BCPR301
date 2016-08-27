"""
Test the correct views

>>> p = Product("O hai", 20, 20, "http://wwww.rawr", "10/10/16", 125)
>>> p.get_views()
125

>>> p.get_dollars()
20

>>> p.get_cents()
20

>>> p.get_price()
'$20.20'

>>> p.get_description()
'O hai'
"""


class Product:
    """
    classdocs
    """

    def __init__(self, the_description,
                 the_dollars,
                 the_cents,
                 the_link,
                 the_date,
                 the_views):
        '''
        Constructor (> ^_^ )>
        '''
        self.description = the_description
        self.dollars = the_dollars
        self.cents = the_cents
        self.link = the_link
        self.date = the_date
        self.views = the_views

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

    def get_views(self):
        return self.views

    def get_object(self):
        return {"description": self.description,
                "dollars": self.dollars,
                "cents": self.cents,
                "link": self.link,
                "date": self.date,
                "views": self.views
                }


if __name__ == "__main__":
    import doctest
    doctest.testmod()
