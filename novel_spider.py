# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests , sys , os , time , random

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
        for i in range(self.cnt):
            chap = self.chapter[i]
            path = self.get_path(chap)
            if not os.path.exists(path):
                req = requests.get(self.urls[i])
                html = BeautifulSoup(req.text)
                content = html.find_all("div",id="content")
                text = content[0].text.replace('\xa0'*8,'\n\n')
                text = text.replace('\xa0','')
                while True:
                    try:
                        text = text.encode("iso-8859-1").decode('gbk')
                        break
                    except UnicodeEncodeError as err:
                        err_str = str(err)
                        print(err_str)
                        idx1 = err_str.find('position ')+9
                        idx2 = err_str.find(': ',idx1)
                        err_idx = err_str[idx1:idx2]
                        try:
                            err_idx = int(err_idx)
                            text = text[0:err_idx-1]+' '+text[err_idx+1:len(text)]
                        except ValueError as err2:
                            
                        
                text = text[0:text.find('[笔趣')]
                
                self.write_file(path,chap,text)
                sys.stdout.write("  已下载  "+chap+"    %.3f%%  " %  float(i/self.cnt) + '\r\n')
                #except UnicodeEncodeError as err:
                ##'gbk' codec can't encode character '\ufffd' in position 2: illegal multibyte sequence
                #    err_str = str(err)
                #    err_idx = err_str[err_str.find('position ')+9:err_str.find(': illegal')]
                #    err_idx = int(err_idx)
                #    text = text[0:err_idx-1]+' '+text[err_idx+1:len(text)]
                #    self.write_file(path,chap,text)
                #    sys.stdout.write("  已下载  "+chap+"    %.3f%%  " %  float(i/self.cnt) + '\r\n')
                #    #sys.stdout.write("    "+chap+"  下载失败，非法字符  " + '\r\n')
                #if i%10 == 0:
                #    time.sleep(random.uniform(5,10))
                #else:
                #    time.sleep(random.uniform(1,20)*0.1)
                sys.stdout.flush()
            else:
                sys.stdout.write("  "+chap+"  已存在  \r\n")
    
    def get_path(self,chapter):
        path = 'D:/Workspaces/python_learning/download/'+self.title
        if not os.path.exists(path):
            os.makedirs(path)
        return path+'/'+chapter+".txt"
    
    def write_file(self,path,chapter,text):
        with open(path,'w',encoding = 'gbk') as f:
            f.writelines(text)
            f.write('\n\n')

if __name__=="__main__":
    dl = novel_downloader()
    dl.get_urls()
    print('开始下载 '+dl.title)
    dl.get_content()
    print('完成下载 '+dl.title)