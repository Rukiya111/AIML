#Python program
import pandas as pd
data=pd.read_csv("C:/Users/SPTINT-06/Desktop/Dataset/iris.csv")
print(data)
print(data.head(5))
print(data.tail(5))
print(data["SepalLengthCm"])
print(data["PetalWidthCm"])
print(data["Species"])
print(data.info())
print(data.dtypes)
print(data.count())
