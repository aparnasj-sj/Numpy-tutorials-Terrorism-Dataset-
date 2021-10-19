'''
As we knew the Kargil ( in Jammu and Kashmir) War that took place between May 1999 and July 1999 (3 Months) ,so there was a huge conflict in Kashmir Valley during this period.
In this dataset, there is no information regarding the war between the two countries to find out the casualty during the war.
So find out the attack in this period in which maximum casualties happened.
Print the count of casualties (as integer), city in which that attack happened and name of attack group.
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
       
        if(row['Year']=='1999' and (row['Month']=='5' or row['Month']=='6' or row['Month']=='7') and row['State']=='Jammu and Kashmir'):
            if 'Unknown' not in row['City'] and 'Unknown' not in row['Group']:
                killed.append(row['Killed'])
                wounded.append(row['Wounded'])
                city.append(row['City'])
                agrp.append(row['Group'])
killed=np.array(killed) #Nd
wounded=np.array(wounded)

city=np.array(city)
agrp=np.array(agrp)

killed[killed=='']='0.0'#eal NULL val
wounded[wounded=='']='0.0'

killed=np.array(killed,dtype=float) #cpnvert float
wounded=np.array(wounded,dtype=float) 

casuality=killed+wounded #calulctae
size=np.size(casuality)
size2=np.size(city)

 

max_so_far=0.0
c=""
grp=""
for i in range(size):
   # print(city[i])
    if(casuality[i]>max_so_far ):
        max_so_far=casuality[i]
        c=city[i]
        grp=agrp[i]
print(int(max_so_far),c,grp)
        
        
    
