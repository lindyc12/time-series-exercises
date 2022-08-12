import pandas as pd
import os
import matplotlib as plt

def clean_store(df):
   df.sale_date = pd.to_datetime(df.sale_date, infer_datetime_format=True)
   df.set_index('sale_date', inplace=True) #make date the index
   df['weekday'] = df.index.day_name()
   df['month'] = df.index.month_name()
   df['sales_total'] = df['sale_amount'] * df['item_price']
   return df

def clean_power(df):
    df.Date = pd.to_datetime(df.Date)
    df.set_index('Date', inplace=True)
    df['day_of_week'] = df.index.strftime('%A')
    df['month'] = df.index.month_name()
    df = df.fillna(0)
    return df
