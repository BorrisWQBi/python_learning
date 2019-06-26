# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__=="__main__":
    #target = "http://gitbook.cn/"
    target = "https://www.biqukan.com/1_1094/5403177.html"
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all("div",id="content")
    v1 = texts[0].text.encode("iso-8859-1")
    print(v1.decode("gbk"))