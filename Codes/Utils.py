import csv
from operator import itemgetter
import os
import sys
import json

def loadjson(filename):
    """Load json file from filename."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def loadcsv(path):
    with open(path, 'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def savecsv(path,csvdata):
    """Save csv file to path."""
    with open(path, 'w', newline='',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(csvdata)


def uniquevalues(path):
    uniquevalues = []
    uniquetexts = []


    documents = os.listdir(os.path.join(sys.argv[1]))
    for file in documents:
        annotations = loadcsv(os.path.join(sys.argv[1], file))
        for line in annotations:
            value = line[1]
            if [value] not in uniquevalues:
                uniquevalues.append([value])

            text = line[0]
            if [text,int(line[2])] not in uniquetexts:
                uniquetexts.append([text,int(line[2])])

    uniquevalues = sorted(uniquevalues)
    uniquetexts = sorted(uniquetexts,key=itemgetter(1))

    return uniquevalues,uniquetexts

def findunique(values):
    unique = []
    for word in values:
        if word not in unique:
            unique.append(word)
    return unique

def checkifexist(word,array):
    for i in range(len(array)):
        if array[i][0] == word:
            return True
    return False

def getid(word,array):
    for i in range(len(array)):
        if array[i][0] == word:
            return i
        
def checkoverlap(verses,value,start,end):
    for verse in verses:
        character = verse[1]
        vstart = verse[2]
        vend = verse[3]
        if int(vstart) <= int(start) and int(vend) >= int(end):
            return character
    for verse in verses:
        character = verse[1]
        vstart = verse[2]
        vend = verse[3]
        print(vstart,start,end,vend)
        print(vstart <= start and vend >= end)
    return False

def textindata(text,data):
    flag = False
    i = 0
    for i in range(len(data)):
        if text == data[i][0]:
            flag = True
            break
    return flag,i


