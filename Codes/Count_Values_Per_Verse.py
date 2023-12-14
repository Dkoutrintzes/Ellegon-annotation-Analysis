import csv
from itertools import count
from math import e, exp
import os
from re import T
import datetime
import sys
from Utils import loadcsv,savecsv,findunique,checkifexist,getid,checkoverlap,textindata
import tkinter as tk 
from tkinter.filedialog import askopenfilename

# 4 arguments are needed:
# 1.Path to the folder containing the csv files
# 2.Path to the folder where the csv files will be saved
# 3.If the values are curated or not
# 4.If the sentences are curated or not

if __name__ == '__main__':
    if not os.path.isdir(sys.argv[2]):
        os.mkdir(sys.argv[2])

    if sys.argv[3] == 'True':
        translation = True
        print('Select the translation file')
        translation_file = askopenfilename()

        translation_dic = {}
        for line in loadcsv(translation_file):
            translation_dic[line[0].replace(" ",'')] = line[1].replace(" ",'')
    else:
        translation = False

    values_dic = {}
    if sys.argv[4] == 'True':
        curation = True
        # Value Curations
        print('Select the curation file')
        values_file = askopenfilename()
        curation_values = loadcsv(values_file)
        for line in curation_values:
            word = line[1].replace(" ",'')
            if translation:
                word = translation_dic[word]
            values_dic[line[0]] = word
    else:
        curation = False


    print('Select the file with the annotated verses')
    characterverse = askopenfilename()
    characterverse = loadcsv(characterverse)
    characters = findunique([word[1] for word in characterverse])

    extdata = []


    paths = os.listdir(os.path.join(sys.argv[1]))
    for path in paths:
        if os.path.isfile(os.path.join(sys.argv[1],path)):
            if path.endswith('.csv'):
                annotations = loadcsv(os.path.join(sys.argv[1],path))
                for line in annotations:
                    text = line[0]
                    value = line[1]
                    start = line[2]
                    end = line[3]       

                    temp = checkoverlap(characterverse,text,start,end)
                    if temp != False:
                        flag, index = textindata(temp, extdata)
                        if flag:
                            if curation:
                                extdata[index].append(values_dic[value])
                            else:
                                extdata[index].append(value)                           
                        else:
                            if curation:
                                tline = [temp,start,values_dic[value]]
                            else:
                                tline = [temp,start,value]
                            extdata.append(tline)  

        elif os.path.isdir(os.path.join(sys.argv[1],path)):
            subpaths = os.listdir(os.path.join(sys.argv[1],path))
            for subpath in subpaths:
                if subpath.endswith('.csv'):
                    annotations = loadcsv(os.path.join(sys.argv[1],path))
                    for line in annotations:
                        text = line[0]
                        value = line[1]
                        start = line[2]
                        end = line[3]       

                        temp = checkoverlap(characterverse,text,start,end)
                        if temp != False:
                            flag, index = textindata(temp, extdata)
                            if flag:
                                if curation:
                                    extdata[index].append(values_dic[value])
                                else:
                                    extdata[index].append(value)                           
                            else:
                                if curation:
                                    tline = [temp,start,values_dic[value]]
                                else:
                                    tline = [temp,start,value]
                                extdata.append(tline)  
                    


    exp_ch_data = []
    for line in extdata:
        temp = []
        name = line[0]
        start = line[1]
        values = line[2:]
        unique = findunique(values)

        temp.append(name)
        temp.append(len(values))
        temp.append(len(unique))
        
        unique_temp = []
        for value in unique:
            unique_temp.append([value,values.count(value)])
        unique_temp = sorted(unique_temp,key=lambda x:x[1],reverse=True)

        for u_line in unique_temp:
            temp.append(u_line[0])
            temp.append(u_line[1])
        exp_ch_data.append(temp)
    
    exp_ch_data = sorted(exp_ch_data,key=lambda x:int(x[1]),reverse=True)

    expname = 'PerVerse.csv'
    count = 1
    while True:
        
        if os.path.isfile(os.path.join(sys.argv[2],expname)):
            expname = 'PerVerse_'+str(datetime.datetime.now()).split(' ')[0]+'_'+str(count)+'.csv'
            count += 1
        else:
            break
    
    savecsv(os.path.join(sys.argv[2],expname),exp_ch_data)
