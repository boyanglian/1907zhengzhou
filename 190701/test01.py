"""
爬虫案例： 查询名字和URL
"""

import requests
r = requests.get('http://www.wise.xmu.edu.cn/people/faculty')   # print(r)    # <Response [200]>
html = r.content       # print(html) 以字节形式展示的html内容  # b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://ww

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'xml')  # 通过BeautifulSoup类以xml类型解析html  # print(soup)  # <?xml version="1.0" encoding="utf-8"?><!DOCTYPE html
div_people_list = soup.find('div', attrs={'class': 'people_list'}) # print(div_people_list)
a_s = div_people_list.find_all('a', attrs={'target': '_blank'})  # print(a_s)

for a in a_s:
    url = a['href']
    name = a.get_text()
    print(name, url)
