import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("adult.data.csv")

print("Columns:")
print(df.columns)

'''plt.figure()
df['age'].hist()
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution")
plt.show()'''

#print(df.head(10))

print(df['age'].mean())