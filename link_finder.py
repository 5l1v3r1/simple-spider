# -*- coding:utf-8 -*-
from HTMLParser import HTMLParser
import os
import urllib2


class MyHTMLParser(HTMLParser):
    def __init__(self, page_url, domain_name):
        '''
           要求url一定是完整的绝对路径,最好带上默认文件名
        '''
        HTMLParser.__init__(self)
        self.htmldata = htmldata
        self.domian_name = domian_name #jwc.uestc.edu.cn or www.baidu.com or baidu.com
        self.directory = self.__Get_Dir(page_url)
        self.links = []

    def __Get_Dir(self,url):
        #有个错误,需要除开?
        return os.path.split(url)[0]+'/'
        

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if len(attrs) == 0:pass
            else:
                for name,value in attrs:
                    if name == "href":
                        if value.find("http")==0 and value.find(domain.name)!=-1:
                            self.links.append(value)
                        if value.find('/')==0:
                            self.links.append(self.domain_name+value)
                        else:
                            self.links.appned(self.directory+value)
                            


def LinkFinder(page_url, domain_name):
    req = urllib2.Request(page_url)
    f = urllib2.urlopen(req)
    html_parser = MyHTMLParser()
    html_parser.feed(f.read())
    html_parser.close()
    return html_parser.links



    
    
    
    
    
