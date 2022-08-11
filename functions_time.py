import pandas as pd
import os
import matplotlib as plt

def clean_store(df):
   df.sale_date = pd.to_datetime('Jan:1:1970', format='%b:%d:%Y')
   df = df.set_index('sale_date').sort_index() #make date the index
   df['weekday'] = df.index.day_name()
   df['month'] = df.index.month_name()
   df['sales_total'] = df['sale_amount'] * df['item_price']
   return df

def clean_power(df):
    df.Date = pd.to_datetime('Jan:1:1970', format='%b:%d:%Y')
    df = df.set_index('Date').sort_index()
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    df = df.fillna(0)
    return df
