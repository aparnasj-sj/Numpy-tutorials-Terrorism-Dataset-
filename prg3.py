'''
Find the casualty in the Red Corridor States ? Mainly Red corridor states include Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh.
Note: Casualty=Killed +Wounded
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
    #flist=list(fdata)
    for row in fdata:
       
       
        if(row['State']=='Andhra Pradesh' or row['State']=='Jharkhand' or row['State']=='Odisha'or row['State']=='Chhattisgarh'):
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
            
killed=np.array(killed) #Nd
wounded=np.array(wounded)


killed[killed=='']='0.0'#eal NULL val
wounded[wounded=='']='0.0'

killed=np.array(killed,dtype=float) #cpnvert float
wounded=np.array(wounded,dtype=float) 

casuality=killed+wounded #calulctae
size=np.size(casuality)
size2=np.size(city)

 


for i in range(size):
   count+=casuality[i]
print(int(count))
