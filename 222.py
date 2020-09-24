import requests
from bs4 import BeautifulSoup
import re

h = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
r = requests.get('http://book.zongheng.com/store.html', headers=h)
# c=r.content
c = r.text

soup = BeautifulSoup(c, 'html5lib')
store_collist = soup.find('div', {'class': 'store_collist'})

pattern = re.compile(r'bookbox f(.)')
book_list = store_collist.find_all('div', {'class': pattern})

books = []
for item in book_list:
    book = {}
    book['bookimg'] = item.find('div', {'class': 'bookimg'}).find('img')['src']
    bookinfo = item.find('div', {'class': 'bookinfo'})
    book['bookname'] = bookinfo.find('div', {'class': 'bookname'}).find('a').text
    book['bookintro'] = bookinfo.find('div', {'class': 'bookintro'}).text

    with open('222/' + book['bookname'] + '.jpg', 'wb') as p:
        s1= requests.get(book['bookimg'])
        s2 = s1.content
        p.write(s2)

    books.append(book)
print(books[1])