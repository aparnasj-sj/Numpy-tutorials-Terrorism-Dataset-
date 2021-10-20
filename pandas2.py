'''
Find the frequency of the Casualty in Red Corridor states and in Jammu and Kashmir ?Here Frequency is (Total Casualty/Total Number of a year)
Print frequency as integer value.
Note:Red Corridor state includes Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh. Here Casualty=Killed +Wounded.Don't fill the nan value present in Killed and Wounded feature.
'''
import pandas as pd
data = pd.read_csv("terrorismData.csv")
data["Casualty"] = data.Killed + data.Wounded
data_1 = data[data.State == "Jammu and Kashmir"]
data_2 = data[(data.State == "Jharkhand") | (data.State == "Odisha") | (data.State == "Andhra Pradesh") | (data.State == "Chhattisgarh")]
sum_1 = data_1.Casualty.sum()
sum_2 = data_2.Casualty.sum()
year = len(set(data['Year']))

print(int(sum_2//year),int(sum_1//year))
