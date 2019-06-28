# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__=="__main__":
    #target = "https://www.biqukan.com/2_2932/1287113.html"
    #req = requests.get(target)
    #html = BeautifulSoup(req.text)
    #text = html.find_all("div",id="content")
    #text = text[0].text.replace('\xa0'*8,'\n\n').encode("iso-8859-1").decode('gbk')
    #print(text)
    err_str = '\'gbk\' codec can\'t encode character \'\ufffd\' in position 2: illegal multibyte sequence'
    print(err_str)
    idx1 = err_str.find('position ')+8
    idx2 = err_str.find(': ',idx1)
    err_idx = err_str[idx1:idx2]
    err_idx = int(err_idx)
    print(err_idx)