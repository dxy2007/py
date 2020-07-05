import requests as r
from bs4 import BeautifulSoup
# code = open('code.html','r').read()
# print(code)
h = {
    'Cokie':'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172a87baebdb-0fd3f75c8f7e5a-15387640-2073600-172a87baebe55%22%2C%22%24device_id%22%3A%22172a87baebdb-0fd3f75c8f7e5a-15387640-2073600-172a87baebe55%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
}
code = r.get('https://d.hetao101.com',headers=h)
code.encoding='UTF-8'
code = code.text
soup = BeautifulSoup(code,'lxml')
for i in soup.select('.remarks'):
    print(i.string)