'''
Find the number of attack held between day 10 and day 20?(ignoring the year and month)(including both day)
Print count of NumberOFAttack as integer value.
'''
import csv 
import numpy as np
count=0
day=[]
with open('terrorismData.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    #flist=list(fdata)
    for row in fdata:
        day.append(row['Day'])
day=np.array(day) #Nd
day[day=='']=-1
day=np.array(day,dtype=float)

for i in day:
    d=int(i)
    
    if(d>=10 and d<=20):
        count+=1
print(count)
