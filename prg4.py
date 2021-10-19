'''
Find top 5 Indian Cities which has most number of casualties ?
Print top 5 cities along with total casualties in that city. Print count of Casualty as integer value.
Note: Ignoring the City which is Unknown.
Casualty = Killed + Wounded.
'''
import csv 
import numpy as np
count=0
killed=[]
wounded=[]
city=[]
agrp=[]
with open('terrorismData.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    
    for row in fdata:
       if(row['Country']=='India' and row['State']!='Unknown' and row['City']!='Unknown'):
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
            city.append(row['City'])
            
killed=np.array(killed) #Nd
wounded=np.array(wounded)


killed[killed=='']='0.0'#eal NULL val
wounded[wounded=='']='0.0'

killed=np.array(killed,dtype=float) #cpnvert float
wounded=np.array(wounded,dtype=float) 

casuality=killed+wounded #calulctae
size=np.size(casuality)
size2=np.size(city)
d={};#dict of (city,count)

 # for each city calculate summation of casulity   
for i in range(size): 
    if(city[i]  in d):
        d[city[i]]+=casuality[i]
    else:
        d[city[i]]=casuality[i]



 #sorted       
d_list = sorted(d.items(), key=lambda x:x[1])
#d_list is list of tuple (key,val) in scending order

d_list.reverse()  #dec order
#convert ot to dict
dict2=dict(d_list)

num=1
for key in dict2:
    if(num>5):
        break
    else:
        print(key,int(dict2[key]))
        num+=1
        


