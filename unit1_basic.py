import pandas as pd
import numpy as np

data = {
    "@Sr.no": [1,2,3,4,5,6,7,8,9,10],
    "Name#": ["LALIT","RINKU","RANHUL","sanjay","arjun","pankaj","ROHIT","praveen","aman","krishan"],
    "Age&": [None,10,None,60,30,None,43,33,32,440],
    "Salary*": [10000,None,30000,40000,50000,None,70000,80000,9000000,None],
    "Typ)e": [None,"temporary","contract",None,"intern","permanent",None,"contract","temparory","intern"],
    "%Status": [None,"married","single","single",None,"married",None,"married","married",None],
    "Exp^rience": [1,None,3,4,5,6,None,None,900,10],
    

}

df = pd.DataFrame(data)


#--------UNIT-1--------
print(df.head())

print(df.tail())

print("information\n",df.info())

print("describe\n",df.describe())

print(df.dtypes)

print(df.columns)

print(df.isnull().sum())

print(df.nunique())

print(df['%Status'].value_counts())

cat_colums = df.select_dtypes(include=object).columns

num_colums = df.select_dtypes(include=['int64','float64']).columns

print(cat_colums)

print(num_colums)

ds = df['Name#'] = df['Name#'].str.lower().str.strip()


print(ds)




