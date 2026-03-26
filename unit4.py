import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
df = pd.read_excel("uncleaned.xlsx")
 


le = LabelEncoder()

#-------Renaming columns--------
df.rename(columns={'@Sr.no':'Sr.no'},inplace=True)
df.rename(columns={'Name#':'Name'},inplace=True)
df.rename(columns={'Age&':'Age'},inplace=True)
df.rename(columns={'Salary*':'Salary'},inplace=True)
df.rename(columns={'Exp^rience':'Exprience'},inplace=True)
# print(df.dtypes)

#convert column to integer or float


df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df.fillna(method='bfill',inplace=True)
df = df[df['Age']<100]

df.drop_duplicates(inplace=True)
df['Name'] = df['Name'].fillna('unknown')
scale = MinMaxScaler()
df[['Age','Salary']] = scale.fit_transform(df[['Age','Salary']])
print(df)
