import pandas as pd
df = pd.read_excel("uncleaned.xlsx")

#------Detect duplicates-------
# print(df.duplicated().sum())
# df = df[df.duplicated()]
# df.drop_duplicates(inplace=True)

#df.drop_duplicates(subset=['Salary*'],inplace=True)  --- This command helps to remove 
# values from the particular columns 

#--------Fixing inconsistent---------
# df['Gender'] = df['Gender'].replace({'M': 'male','F': 'female'})

#--------Checking and validating data--------
df[df['Age&']<0]
df = df[df['Salary*'] < 100000]
print(df)