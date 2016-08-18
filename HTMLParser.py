'''
Created on 18/08/2016

@author: AndrewM
'''
# import bs4
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime
class Scrapper:
    '''
    classdocs

     '''
    '''def __init__(self, params):
    '''
    '''
    Constructor
    '''
    # make private????
    data = [];
    def collect_data(self):
        r = requests.get("http://www.impc.co.nz/products/list/desktop_memory-128-page0.html").text
        soup = BeautifulSoup(r, 'html.parser');
        table = soup.find("table", attrs={'class': 'grid productlist'})
        links = self.get_links(table)
        #links = soup.findAll('a')
        rows = table.find_all('tr')
        second_column = []
        third_column = []
        for row in rows:
            # the contents themselves are in a list format, so target first element to remove that
            third_column.append(row.findAll('td')[2].contents[0])
            second_column.append(row.findAll('td')[1].contents[0])
        price_list = self.get_prices(third_column)
        description = self.get_description(second_column)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data.append(description)
        self.data.append(price_list)
        self.data.append(links)
        self.data.append(date)
#         for stuffs in self.data:
#             for item in stuffs:
#                 print(item)
# 
#         for i in range(2):
#             for item in self.data[i]:
#                 print(item)
#         print(self.data[3])
        
    def get_links(self, table):
        links = []
#       Starts at the 2nd row, and skips every odd row after
        for link in table.findAll('a',href=True)[1::2]:
        #if link.has_attr('href'):
#       the links were relative, so concatenation was used to convert them to absolute
            links.append("http://www.impc.co.nz" + link['href'])
        #print("http://www.impc.co.nz" +link['href'])
        return links
        
    def get_prices(self, column):
        price_list = []
        for price in column:
            dollars = 0
            cents = 0
#           start printing from the first character onwards (to remove the $ symbol
#           cuts off the end of the string starting at the specified character, in this case: '+'
            #print(price[1:].rsplit('+', 1)[0])
            dollars = int(price[1:].rsplit('.', 1)[0])
#           scan past $ symbol and decimal point, thus +2, and scan past the dollars. len doesn't work on ints
            cents = int(price[len(str(dollars))+2:].rsplit('+', 1)[0])
            #price_list.append(price.string)
            price = []
            price.append(dollars)
            price.append(cents)
            price_list.append(price)
            
        return price_list
        
    def get_description(self, column):
        description = []
        for the_description in column:
            description.append((the_description.string))
        return description
    
    def get_data(self):
        return self.data
    

scrapper = Scrapper()

scrapper.collect_data()




