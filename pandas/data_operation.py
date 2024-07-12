import pandas as pd 

print(pd.__version__)

dist= {
  'head':{
    'name':'Ashim J. Karki',
    'address':'kathamndu',
    'number':123456
  },
  'staff1':{
    'name':'Rajesh hamal',
    'address':'lalitpur',
    'number':123999
  }
}
#to convert dictionary to data frame we can use pd.DataFrame
df=pd.DataFrame(dist)
print(df)
print(df.head())
 

#to read datav from csv
df_Csv = pd.read_csv('/Users/ashim/Desktop/Professional course/pandas/ecommerce_sales_analysis.csv')
print(df_Csv)

print(df_Csv.head())
print(df_Csv.tail())
print(df_Csv.describe())
print(df_Csv.info())


print()
 
 