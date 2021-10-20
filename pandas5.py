'''
Find out the Country with Highest Number of Terror Attack and in which year the most number of terrorist attack happened in that country ?
Print count of terror attacks as integer value.
'''
import pandas as pd

df=pd.read_csv("terrorismData.csv")
a=df['Country'].value_counts().idxmax()
df=df[df.Country==a]# only country a

yr=df['Year'].value_counts().idxmax()

print(a,df.shape[0],yr)
