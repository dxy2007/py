# import requests
# headers={
#     'Cookie':'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221726920b926972-00cd1bb54dca3-43450521-2073600-1726920b927502%22%2C%22%24device_id%22%3A%221726920b926972-00cd1bb54dca3-43450521-2073600-1726920b927502%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
#     'Host':'www.hetao101.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
# }
# r = requests.get('https://www.hetao101.com',headers=headers)
# print(r.content.decode('UTF-8'))
import re
import requests
r = requests.get('https://news.qq.com/zt2020/page/feiyan.htm#/global')
code = r.content.decode('GBK')
# print(type(code))
code = re.findall('<td data-v-140d8e16="">(.*?)</td>',code)
print(code)