'''
Most Deadliest attack in a history of HumanKind?
Print count of Killed people as integer value.
Note: Here Deadliest attack means, in which the most number of people killed.
'''
import pandas as pd

df=pd.read_csv("terrorismData.csv")

print(int(df.loc[df['Killed'].idxmax()]['Killed']),df.loc[df['Killed'].idxmax()]['Country'],df.loc[df['Killed'].idxmax()]['Group'])
