"""
Created on 18/08/2016

@author: AndrewM
"""
# import bs4
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime


class Scrapper:
    """
    classdocs
    """
    
    data = {
        "descriptions": None,
        "prices": None,
        "links": None,
        "date": None,
        "views" : None
    }
    
    def __init__(self, the_url=None):
        if the_url is None:
            # PEP8 didn't like the "long" link, had to split it up =.=
            absolute = "http://www.impc.co.nz"
            relative = "/products/list/desktop_memory-128-page0.html"
            self.url = absolute + relative
        '''
        Constructor
        '''
    
    ""

    def collect_data(self):
        # had to put url in variable, because otherwise the line was too long.
        # u = "http://www.impc.co.nz/products/list/desktop_memory-128-page0.html"
        r = requests.get(self.url).text
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.find("table", attrs={'class': 'grid productlist'})
        links = self.get_links(table)
        # links = soup.findAll('a')
        rows = table.find_all('tr')
        second_column = []
        third_column = []
        for row in rows:
            # the contents themselves are in a list format,
            # so target first element to remove that
            third_column.append(row.findAll('td')[2].contents[0])
            second_column.append(row.findAll('td')[1].contents[0])
        price_list = self.get_prices(third_column)
        description = self.get_description(second_column)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data["descriptions"] = description
        self.data["prices"] = price_list
        self.data["links"] = links
        self.data["date"] = date
        page_views = self.get_page_view()
        self.data["views"] = page_views

    def get_links(self, table):
        links = []
        # Starts at the 2nd row, and skips every odd row after
        for link in table.findAll('a', href=True)[1::2]:
            # if link.has_attr('href'):
            # the links were relative,
            # so concatenation was used to convert them to absolute
            links.append("http://www.impc.co.nz" + link['href'])
            # print("http://www.impc.co.nz" +link['href'])
        return links

    def get_prices(self, column):
        price_list = []
        for price in column:
            dollars = 0
            cents = 0
            # start printing from the first character onwards
            # (to remove the $ symbol
            # cuts off the end of the string starting at the
            # specified character, in this case: '+'
            # print(price[1:].rsplit('+', 1)[0])
            dollars = int(price[1:].rsplit('.', 1)[0])
            # scan past $ symbol and decimal point,
            # thus +2, and scan past the dollars. len doesn't work on ints
            cents = int(price[len(str(dollars))+2:].rsplit('+', 1)[0])
            # price_list.append(price.string)
            price = []
            price.append(dollars)
            price.append(cents)
            price_list.append(price)

        return price_list

    def get_description(self, column):
        description = []
        for the_description in column:
            # beautiful soup doesn't actually convert data to string, have to do it yourself, this caused issues.
            description.append((str(the_description.string)))
        return description

    def get_data(self):
        return self.data
    
    def get_page_view(self):
        image_data = []
        count = 1;
        print("Getting page view data...")
        num_links = len(self.data["links"])
        for link in self.data["links"]:
            print("Working on page " + str(count) + " of " + str(num_links) + "...")
            r = requests.get(link).text
            soup = BeautifulSoup(r, 'html.parser')
            image_data.append(str(soup.find("img", attrs={'class': 'imagenumber'})))
            count += 1
        print("Finished.. Collected " + str(len(image_data)) + " of " + str(num_links))
        page_view_data = []
        for datum in image_data:
            # grab the first element of the returned list
            page_view_data.append(int(datum[10:].rsplit('\" class')[0]))
        return page_view_data
