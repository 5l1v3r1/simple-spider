# -*- coding:utf-8 -*-
from special import *
from link_finder import LinkFinder
import os


class Spider:
    #myqueue = Queue.Queue(maxsize = 5) #设置爬虫线程最大数
    show_page_list = ['.html', '.php', '.asp', '.jsp', 'htm', '']
    #下面是在__init__需要初始化的数据
    project_name=''
    target_url=''
    domain_name=''
    hastask=False
    crawled_result_file=''
    config_file=''
    crawled_url=[]

    def __init__(self,project_name, target_url,domain_name,hastask=False):
        Spider.project_name = project_name
        Spider.target_url = target_url
        Spider.domain_name = domain_name
        Spider.hastask = hastask
        Spider.crawled_result_file = project_name + '/crawled_result.txt'
        Spider.config_file = project_name + '/config.txt'
        Spider.crawled_url = [target_url]  #初始化需要爬行的网页链接


        self.boot()
        self.crawl_page(Spider.domain_name)

    @staticmethod  
    def boot():
        create_project_dir(Spider.project_name)
        check_config_file(Spider.project_name,Spider.config_file,Spider.target_url)
        create_config_file(Spider.config_file,Spider.target_url)
        create_data_files(Spider.crawled_result_file)
        Spider.crawled_url += file_to_list(Spider.crawled_result_file)
        
    @staticmethod
    def crawl_page(domain_name):
        print "[+]Begin to crawl "+domain_name
        try:
            for page_url in Spider.crawled_url:
                if Spider.hastask:
                    Spider.task(page_url)
                if os.path.splitext(page_url)[1] in Spider.show_page_list:
                    #有个错误,需要除开?
                    Spider.CheckAndAdd(LinkFinder(page_url,domain_name))
        except KeyboardInterrupt:
            print "[+]Saving result"
            list_to_crawled_result_file(Spider.crawled_result_file,Spider.crawled_url)


    @staticmethod
    def CheckAndAdd(URL_list):
        for url in URL_list:
            if not url in Spider.crawled_url: 
                Spider.crawled_url.append(url)
    

    @staticmethod
    def task(page_url):#对每一个url,进行的操作
        pass
        
            
            









            
            
        
        
        

