# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import os,json
import base64
from prettytable import PrettyTable
import warnings
import datetime

warnings.filterwarnings("ignore")
BASE_URL = 'https://book.douban.com'
_session = requests.session()


class Song(object):
    def __lt__(self, other):
        return self.commentCount > other.commentCount

#获取book
def getBookList():
    pageMax = 10 #共10页
    bookList = []
    for i in range(1,pageMax + 1):
        url ='https://book.douban.com/top250?start='+ str((i-1) * 25)
        url.encode('utf-8')
        bs = BeautifulSoup(_session.get(url).content)
        bookUrlLst = bs.findAll('a', attrs={'class': 'nbg'})#爬取book的url
        for a in bookUrlLst:
            song = Song()
            bookUrl = a['href']
            statusCode = _session.get(bookUrl).status_code #获取浏览器返回的状态码
            if statusCode == 404:
                print("网页没有找到..."+bookUrl)
                continue
            else:
                soup = BeautifulSoup(_session.get(bookUrl).content)
                r = soup.find('a', class_='rating_people').span.string  # 评论次数
                if int(r) >= 100000:
                    print(bookUrl)
                    introSize = soup.findAll('div', attrs={'class': 'intro'})
                    if len(introSize) < 2:
                        song.bookIntro = soup.findAll('div', attrs={'class': 'intro'})[0].p.string  # 内容简介
                    else:
                        song.bookName = soup.find('h1').find("span").get_text() #书名
                        song.bookIntro = soup.findAll('div', attrs={'class': 'intro'})[0].p.string  # 内容简介
                        song.authorIntro = soup.findAll('div', attrs={'class': 'intro'})[1].p.string  # 作者简介
                        song.author = soup.find('div',id='info').span.a.string #作者
                        song.ratingNum = soup.findAll('strong',attrs={'class':'rating_num'})[0].get_text() #评分
                        song.ratingSum = r #评论次数
                        song.path = bookUrl
                        bookList.append(song)

    bookList = list(bookList)
    return bookList


if __name__ == '__main__':
    # soup = BeautifulSoup(_session.get('https://book.douban.com/subject/1963684/').content)
    # bookName = soup.find('h1').find("span").get_text()
    # print(bookName)
    bookList = getBookList()
    for song in bookList:
        print('获取成功{名称:', song.bookName, ',作者:', song.author,'图书简介:',song.bookIntro, ',评分:', song.ratingNum, ',评论数：',song.ratingSum,'地址：',song.path,'}')