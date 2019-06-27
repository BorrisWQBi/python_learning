# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests , sys , os

class novel_downloader(object):
    def __init__(self):
        self.base = "https://www.biqukan.com"
        self.target = "https://www.biqukan.com/2_2932"
        self.title = ''
        self.chapter = []
        self.urls = []
        self.cnt = 0
        
    def get_urls(self):
        req = requests.get(self.target)
        html = req.text
        bf = BeautifulSoup(html)
        
        title = bf.find_all("div",class_="info")
        self.title = title[0].find_all("h2")[0].string
        
        div = bf.find_all("div",class_="listmain")
        div = div[0]
        div = div.find_all('a')
        div = div[12:]
        self.cnt = len(div)
        
        print(self.title+' 共有 '+ str(self.cnt) +' 个章节 ')
        for ele in div :
            self.chapter.append(ele.string)
            self.urls.append(self.base+ele.get('href'))
    
    def get_content(self):
        for i in range(5):
            req = requests.get(self.urls[i])
            chap = self.chapter[i]
            html = BeautifulSoup(req.text)
            text = html.find_all("div",id="content")
            text = text[0].text.replace('\xa0'*8,'\n\n').encode("iso-8859-1").decode('gbk')
            self.write_file(chap,text)
            sys.stdout.write("  已下载:%.3f%%" %  float(i/self.cnt) + '\r')
            sys.stdout.flush()
            
    def write_file(self,chapter,text):
        path = '/mnt/c/ProjectSpace/download/'+self.title
        if not os.path.exists(path):
            os.makedirs(path)    
        with open(path+'/'+chapter+".txt",'w',encoding='gbk') as f:
            f.write(chapter + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__=="__main__":
    dl = novel_downloader()
    dl.get_urls()
    print('开始下载 '+dl.title)
    dl.get_content()
    print('完成下载 '+dl.title)