'''
Problem Statement :
Find the most frequent day of attack in a terrorismDataset ?
Note: Here np.unique can be used.
Print count of frequent day and number of attack as Integer value.
'''
import csv 
import numpy as np
count=0
day=[]
num=[]

with open('terrorismData.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    
    for row in fdata:
            day.append(row['Day'])
            
day=np.array(day)          
# first way using np.unqi=ue 
unique,count=np.unique(day,return_counts=True)
#find index of maximun
ind=count.argmax()
print(unique[ind],count[ind])
