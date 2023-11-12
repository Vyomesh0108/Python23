import pandas as pd

# Pandas library works with the Data Sets: Analyzing, Cleaning, Exploring and Manipulating Data.
# 3 Data Structure: Series, DataFrame, Panel
# Series: 1D Array - Homogeneous - one datatype
# DataFrame: 2D Array - Heterogeneous - different datatype - Rows & Columns
# Panel: 3D Array - Container for DataFrame

data = [11, 12, 13, 14, 15]
df = pd.DataFrame(data)
print(df)
print("")

# column keyword is used to change the name of columns
data1 = [['Alex', 23], ['Emma', 18], ['Tom', 20]]
df = pd.DataFrame(data1, columns=["Name", "Age"])
print(df)
print("")

data2 = {'Name': ['Alex', 'Emma', 'Tom'], 'Age': [23, 18, 20]}
df = pd.DataFrame(data2, columns=["Name", "Age"])
print(df)
print("")

# index keyword is used to change the name of the rows
data3 = {'Name': ['Alex', 'Emma', 'Tom'], 'Age': [23, 18, 20]}
df = pd.DataFrame(data3, index=['Row1', 'Row2', 'Row3'])
print(df)
print("")

df = pd.read_csv('data.csv')
print(df)
print("")
# Custom View
# By default first 5 Rows
print(df.head())
print("")
# First 10 Rows
print(df.head(10))
print("")
# By default last 5 Rows
print(df.tail())
print("")
# Last 10 Rows
print(df.tail(10))
print("")

# Information about Life
print(df.info())
print("")

df1 = pd.read_csv('dirtydata.csv')
print(df1)
print("")
print(df1.info())
print("")
print(df1.head())
print("")
print(df1.tail())
print("")

# Removes Null Value Rows
new_df = df1.dropna()
print(new_df)
print("")
# df1.fillna(200, inplace=True)
# print(df1)
# print("")

# df1['Calories'].fillna(200, inplace=True)
# print(df1)
# print("")

df1['Date'].fillna(200, inplace=True)
print(df1)