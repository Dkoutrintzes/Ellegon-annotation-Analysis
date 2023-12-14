import csv
from itertools import count
from math import e, exp
import os
from re import T
import datetime
import sys
from Utils import loadcsv,savecsv,findunique,checkifexist,getid
import tkinter as tk 
from tkinter.filedialog import askopenfilename

def scrap_annotation(path,count_val,curation,curation_dic,phrase_curation,phrase_dic,exp_data):
    annotations = loadcsv(path)
    for annotation in annotations:
        value = annotation[1]
        if curation:
            count_val[curation_dic[value]] += 1
        else:
            if value not in count_val.keys():
                count_val[value] = 1
            else:
                count_val[value] += 1
        

        text = annotation[0]
        if phrase_curation:
            text = phrase_dic[text]

        if text == 'Skip':
            continue
        
        flag = checkifexist(text,exp_data)
        if flag:
            id = getid(text,exp_data)
            if curation:
                exp_data[id][1].append(curation_dic[value])
            else:
                exp_data[id][1].append(value)
        else:
            if curation:
                exp_data.append([text,[curation_dic[value]]])
            else:
                exp_data.append([text,[value]])
    return count_val,exp_data



# 5 arguments are needed:
# 1.Path to the folder containing the csv files
# 2.Path to the folder where the csv files will be saved
# 3.If the values are translated or not
# 4.If the values are curated or not
# 5.If the sentences are curated or not


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
    count_val = {}
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
            count_val[word] = 0
    else:
        curation = False
        
    phrase_dic = {}
    if sys.argv[5] == 'True':
        phrase_curation = True
        # Phrase Curations
        print('Select the phrase curation file')
        phrase_curation_file = askopenfilename()
        for line in loadcsv(phrase_curation_file):
            phrase_dic[line[0]] = line[1]   
    else:
        phrase_curation = False                        
    
    exp_data = []
 
    paths = os.listdir(os.path.join(sys.argv[1]))

    for path in paths:
        if os.path.isfile(os.path.join(sys.argv[1],path)):
            if path.endswith('.csv'):
                count_val,exp_data = scrap_annotation(os.path.join(sys.argv[1],path),count_val,curation,values_dic,phrase_curation,phrase_dic,exp_data)
        elif os.path.isdir(os.path.join(sys.argv[1],path)):
            subpaths = os.listdir(os.path.join(sys.argv[1],path))
            for subpath in subpaths:
                if subpath.endswith('.csv'):
                    count_val,exp_data = scrap_annotation(os.path.join(sys.argv[1],path,subpath),count_val,curation,values_dic,phrase_curation,phrase_dic,exp_data)

        


    exp_values_freq = []
    for key in count_val:
        exp_values_freq.append([key,count_val[key]])
    
    exp_freqperph= []
    for line in exp_data:
        temp = []
        text = line[0]
        if text == 'Skip':
            continue
        temp.append(text)
        values = line[1]
        num_values = len(values)
        temp.append(num_values)
        unique = findunique(values)
        temp.append(len(unique))
        count_unique = []
        for value in unique:
            count_unique.append([value,values.count(value)])
        count_unique = sorted(count_unique,key=lambda x:x[1],reverse=True)

        for line in count_unique:
            temp.append(line[0])
            temp.append(line[1])
        exp_freqperph.append(temp)
    
    exp_values_freq = sorted(exp_values_freq,key=lambda x:x[1],reverse=True)
    exp_freqperph = sorted(exp_freqperph,key=lambda x:x[1],reverse=True)

    valfname = 'ValueFrequencies.csv'
    count = 1
    while True:
        
        if os.path.isfile(os.path.join(sys.argv[2],valfname)):
            valfname = 'ValueFrequencies_'+str(datetime.datetime.now()).split(' ')[0]+'_'+str(count)+'.csv'
            count += 1
        else:
            break
            
    savecsv(os.path.join(sys.argv[2],valfname),exp_values_freq)

    phname = 'ValuesFreqPerSent.csv'
    count = 1
    while True:
        
        if os.path.isfile(os.path.join(sys.argv[2],phname)):
            phname = 'ValuesFreqPerSent_'+str(datetime.datetime.now()).split(' ')[0]+'_'+str(count)+'.csv'
            count += 1
        else:
            break

    savecsv(os.path.join(sys.argv[2],phname),exp_freqperph)





