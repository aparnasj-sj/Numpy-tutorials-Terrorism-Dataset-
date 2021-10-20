'''
The Most Dangerous city in Jammu and Kashmir and the terrorist group which is most active in that city?
Print count of number of attacks in that city as integer value.
'''
import pandas as pd

df=pd.read_csv("terrorismData.csv")
#df not dataFrame
df2=df[df.State=='Jammu and Kashmir']
#print(df2.shape)
city=df2.City.value_counts().idxmax()

print(city,end=" ")
df3=df2[df2.City==city] # only city srinagar
df3.drop(df3.loc[df3['Group'] == 'Unknown'].index, inplace=True) # remove rows whose col for grp 'Unknown'

print(df2[df2.City==city].shape[0],end=" ")

grp=df3.Group.value_counts().idxmax()
print(grp)


'''
https://www.w3resource.com/pandas/series/series-value_counts.php
'''
