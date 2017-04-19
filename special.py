# -*- coding:utf-8 -*-
import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

def create_data_files(crawled_result):
    if not os.path.isfile(crawled_result):
        write_file(crawled_result,'')

def check_config_file(project_name,config_file,target_url):
    try:
        with open(config_file,'r') as f:
            if f.read() != target_url:
                print "[-]Project ("+project_name+") should only have one target_url!!"
                exit(1)
    except:
        pass

def create_config_file(config_file, target_url):
    with open(config_file,'w') as f:
        f.write(target_url)

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)  


def file_to_list(file_name):
    results = []
    with open(file_name,'r') as f:
        for line in f.readlines():
            results.append(line.strip('\n'))
    return results
        
def list_to_crawled_result_file(result_file,url_list):
    with open(result_file,'w') as f:
        for url in url_list:
            f.write(url+'\n')
    
    
                           
                           
