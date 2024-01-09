# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


def feature_type (ftype):
    db = pd.read_csv(r'C:\Users\ajohnson\Downloads\{}.csv'.format(ftype), header = None)

    temp = []
    for i in db:
        db[i]=('\'' +  db[i] + '\'')
        temp.append (db[i])
        
    df = pd.DataFrame(temp)
    print(df)
    df.to_csv(r'C:\Users\ajohnson\Downloads\{}.txt'.format(ftype), index = False)

f1 = 'sa' #service address
f2 = 'fse' #fiber splice enclosure
f3 = 'sp' #fiber splitter
f4 = 'fc' #fibe cable
f5 = 'sl' #slack loop
f6 = 'ap' #access point
f7 = 'conduit'

feature_type (f1)









# db = pd.read_csv(r'C:\Users\ajohnson\Downloads\fse.csv')

# temp = []
# for i in db:
#     db[i]=('\'' +  db[i] + '\'')
#     temp.append (db[i])
    
# df = pd.DataFrame(temp)
# print(df)
# df.to_csv(r'C:\Users\ajohnson\Downloads\fse.txt', index = False)