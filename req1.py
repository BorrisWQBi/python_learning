# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__=="__main__":
    target = "https://www.biqukan.com/2_2932/1286972.html"
    req = requests.get(target)
    html = BeautifulSoup(req.text)
    text = html.find_all("div",id="content")
    text = text[0].text.replace('\xa0'*8,'\n\n').encode("iso-8859-1").decode('gbk')
    print(text)