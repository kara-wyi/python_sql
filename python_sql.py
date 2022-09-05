import pandas as pd
from pandasql import sqldf
import datetime 

# sqlite3 order.db
# .mode csv
# .import orders.csv orders
# SELECT .. ;
# .schema ; 
# CREATE TABLE test;

#read in pc case study data and formatting
df = pd.read_csv('pc/orders.csv')
df['Created_Week'] = pd.to_datetime(df['Created_Week'])
for col in ['Order_ID','Order_Cohort','Customer_ID']:
    df[col] = df[col].astype(str)
print(df.dtypes)


#function to run sql query and save query result in csv
def sql_result(q, file_name: str):
    """run sql query then save result in csv, return result"""
    result = sqldf(q)
    result.to_csv(f'{file_name}.csv',index = False)
    return result


#example query
q = """

SELECT 
Created_Week,
ROW_NUMBER() OVER (ORDER BY Created_Week) AS nth_week

FROM (
SELECT 
    distinct Created_Week
FROM df
)
"""
week_count = sql_result(q, "week_count")