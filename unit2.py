import pandas as pd

data = {
    "@Sr.no": [1,2,3,4,5,6,7,8,9,10],
    "Name#": ["LALIT","RINKU",None,"sanjay","arjun","pankaj","ROHIT","praveen","aman","krishan"],
    "Age&": [None,10,None,60,30,None,43,33,32,440],
    "Salary*": [10000,None,30000,40000,50000,None,70000,80000,9000000,None],
    "Typ)e": [None,"temporary","contract",None,"intern","permanent",None,"contract","temparory","intern"],
    "%Status": [None,"married","single","single",None,"married",None,"married","married",None],
    "Exp^rience": [1,None,3,4,5,6,None,None,900,10],
    
}

df = pd.DataFrame(data)
# print(df)
#----------1.Detect missing data-----------

# print(df.isnull().sum())

# print(df.isnull().values.any())

#-----------2. Remove missing data------------

# df.dropna(inplace=True)

# df.dropna(axis=1,inplace=True)

# df.dropna(subset=['Age&'],inplace=True)

##----------3. Replacing Missing values#----------

# df.fillna(0,inplace=True)

# df['Age&'].fillna(0,inplace=True)

# df['Exp^rience'].fillna(df['Exp^rience'].median(),inplace=True)

# df['Exp^rience'].fillna(df['Exp^rience'].mean(),inplace=True)

# df['Exp^rience'].fillna(df['Exp^rience'].mode()[0],inplace=True)

# df.fillna(method='ffill',inplace=True)

# df.fillna(method='bfill',inplace=True)

print("Drop Rows\n",df)

