import pandas as pd

df=pd.read_csv('C:/Users/10827467/OneDrive - LTIMindtree/Desktop/Data Engineering/Sales.csv')
# print(df['product'])
df['total_amount']=df['quantity']*df['price']
high_value=df[df['total_amount']>2000]
print(high_value)