from genericpath import isfile
import json
import os
import csv
import pandas as pd
import sys
from Utils import loadcsv,savecsv,loadjson

def read_collection(data,savepath):
    documents = data['data']['documents']
    for doc in documents:
        annotation = doc['annotations']
        name = doc['name']
        print(name)

        fulltext = doc['text']
        csvdata = []
        for ano in annotation:
            if len(ano['spans']) > 0:
                start = ano['spans'][0]['start']
                end = ano['spans'][0]['end']
                text = ano['spans'][0]['segment']
                value = ano['attributes'][0]['value']
                csvdata.append([text, value, start, end])
                #print('Text: '+text+' has value of: '+value+' from '+str(start)+' to '+str(end))
                #print('-----------------------')

        csvname = name.split('.')[0]+'.csv'
        t=1
        while os.path.isfile(os.path.join(savepath, csvname)):
            csvname = name.split('.')[0]+'_'+str(t)+'.csv'
            t+=1
        savecsv(os.path.join(savepath, csvname),csvdata)
        
# 2 arguments are needed:        
# 1.Path to the json file or folder containing json files
# 2.Path to the folder where the csv files will be saved
if __name__ == '__main__':
    path =  sys.argv[1]
    savepath = sys.argv[2]
    if not os.path.isdir(savepath):
        os.mkdir(savepath)
    if os.path.isfile(path):
        data = loadjson(path)
        read_collection(data,savepath)
    elif os.path.isdir(path):
        files = os.listdir(path)
        print(files)
        for file in files:
            if file.endswith('.json'):
                data = loadjson(os.path.join(path, file))
                read_collection(data,savepath)
            



