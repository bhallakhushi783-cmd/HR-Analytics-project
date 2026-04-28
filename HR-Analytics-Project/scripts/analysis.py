import pandas as pd
import matplotlib.pyplot as plt

# file load
df = pd.read_csv("data/employees.csv")

# first look
print(df.head())

# basic info
print(df.info())

# duplicate check
print("Duplicates:",df.duplicated().sum())

# duplicate check
df = df.drop_duplicates()

# attrition into numeric
df['Attrition_Flag'] = df['Attrition'].map({'Yes' : 1, 'No' : 0})

# Salary level
df['Salary_Level'] = pd.cut(df['Salary'],
                           bins=[0, 40000, 60000, 100000],
                           labels=['Low', 'Medium', 'High'])

# Tenure group
df['Tenure_Group'] = pd.cut(df['Years_at_Company'],
                           bins=[0, 2, 5, 20],
                           labels=['0-2', '2-5', '5+'])


# Attrition rate
attrition_rate = df['Attrition_Flag'].mean()
print("Attrition Rate:", attrition_rate)

# Avg salary (Yes vs No)
print(df.groupby('Attrition')['Salary'].mean())

# Department-wise attrition
print(df.groupby(['Department', 'Attrition']).size())

# Satisfaction vs attrition
print(df.groupby('Attrition')['Job_Satisfaction'].mean())

# Attrition count
df['Attrition'].value_counts().plot(kind='bar')
plt.title("Attrition Count")
plt.show()

# Salary by attrition
df.groupby('Attrition')['Salary'].mean().plot(kind='bar')
plt.title("Average Salary by Attrition")
plt.show()