# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import warnings
import re

BASE_URL = 'http://www.555zw.com/book/34/34512/'
warnings.filterwarnings("ignore")
_session = requests.session()

#获取book
def getBook():
    bs = BeautifulSoup(_session.get(BASE_URL).content)
    table = bs.find('div',attrs={'class':'dir'}).find('table')
    for row in table.findAll('tr'):
        for tr in row.findAll('a'):
            print(tr)





if __name__ == '__main__':
    getBook()