import pandas as pd 
crime_df=pd.read_csv('/Users/ashim/Desktop/Professional course/pandas/SouthAfricaCrimeStats_v2.csv')

print(crime_df)

print(crime_df.head)
print(crime_df.tail)
print(crime_df.isnull().sum())
