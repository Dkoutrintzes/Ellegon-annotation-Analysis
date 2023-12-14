import csv
from operator import itemgetter
import os
import datetime
import sys
from Utils import loadcsv,savecsv

if __name__ == '__main__':
    uniquevalues = []
    uniquetexts = []
    if not os.path.isdir(sys.argv[2]):
        os.mkdir(sys.argv[2])

    paths = os.listdir(os.path.join(sys.argv[1]))
    for path in paths:
        if os.path.isfile(os.path.join(sys.argv[1],path)):
            if path.endswith('.csv'):
                annotations = loadcsv(os.path.join(sys.argv[1],path))
                for line in annotations:
                    value = line[1]
                    if [value] not in uniquevalues:
                        uniquevalues.append([value])

                    text = line[0]
                    if [text,int(line[2])] not in uniquetexts:
                        uniquetexts.append([text,int(line[2])])
        elif os.path.isdir(os.path.join(sys.argv[1],path)):
            subpaths = os.listdir(os.path.join(sys.argv[1],path))
            for subpath in subpaths:
                if subpath.endswith('.csv'):  
                    annotations = loadcsv(os.path.join(sys.argv[1],path))
                    for line in annotations:
                        value = line[1]
                        if [value] not in uniquevalues:
                            uniquevalues.append([value])

                        text = line[0]
                        if [text,int(line[2])] not in uniquetexts:
                            uniquetexts.append([text,int(line[2])])   


    print('len of values: ',len(uniquevalues))
    print('len of texts: ',len(uniquetexts))
    uniquevalues = sorted(uniquevalues)
    uniquetexts = sorted(uniquetexts,key=itemgetter(1))
    Unq_val_name = 'uniquevalues.csv'
    count = 1
    while True:
        if os.path.isfile(os.path.join(sys.argv[2],Unq_val_name)):
            Unq_val_name = 'uniquevalues' +str(datetime.datetime.now()).split(' ')[0]+'_'+ str(count) + '.csv'
            count += 1
        else:
            break
    
    
    Unq_text_name = 'uniquetexts.csv'
    
    count = 1
    while True:
        if os.path.isfile(os.path.join(sys.argv[2],Unq_text_name)):
            Unq_text_name = 'uniquetexts' +str(datetime.datetime.now()).split(' ')[0]+'_'+ str(count) + '.csv'
            count += 1
        else:
            break


    savecsv(os.path.join(sys.argv[2],Unq_val_name),uniquevalues)
    savecsv(os.path.join(sys.argv[2],Unq_text_name),uniquetexts)

