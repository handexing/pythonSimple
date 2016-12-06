# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import warnings
import re

BASE_URL = 'http://www.555zw.com/book/34/34512/'
warnings.filterwarnings("ignore")
_session = requests.session()

#��
class Book(object):
    def __lt__(self, other):
        return self.id > other.id

#�½�
class Chapter(object):
    def __lt__(self, other):
        return self.id > other.id


#��ȡbook
def getBook():
    bookList = []
    bs = BeautifulSoup(_session.get(BASE_URL).content)
    table = bs.find('div',attrs={'class':'dir'}).find('table')
    for row in table.findAll('tr'):
        for tr in row.findAll('a'):
            book = Book()
            book.name=tr.text
            book.url=tr.get('href')
            bookList.append(book);
    bookList.pop()
    print("#################ͼ���ַ��ȡ��ϣ�����"+str(len(bookList))+"���£�##############")
    return bookList


def getChapter():
    bookList = getBook()
    chapterList = []
    for book in bookList:
        chapter = Chapter()
        bs = BeautifulSoup(_session.get(BASE_URL+book.url).content)
        chapter.name = bs.find('div',attrs={'class':'article_listtitle'}).get_text();
        chapter.content = bs.find('div',attrs={'id':'content'}).get_text()
        chapterList.append(chapter)
        print(BASE_URL+book.url)
    print("#################�½ڻ�ȡ��ϣ�##############")
    return chapterList

#������д���ı��ļ�
def record():
    file = open('wmsj.txt','w')
    chapterList = getChapter()
    print("#################��ʼд�����ݣ�����" + str(len(chapterList)) + "���£�##############")
    try:
        for chapter in chapterList:
            file.write("��"+chapter.name+"��")
            file.write('\n')
            file.write(chapter.content.replace(u'\xa0', u' ') )
            file.write("\n==================================���½���==================================")
            print("#################�ɹ�д��һ����ϣ�##############")
    finally:
        file.close()


if __name__ == '__main__':
    record()
    print("#################������ϣ�##############")
