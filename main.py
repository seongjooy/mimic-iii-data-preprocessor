import random
import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
import vitals_extractor
import csv_file_process
import sample_chart
import csv_pivot_and_reformat
import vitals_id
import datetime
from datetime import datetime

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# 'chart_events_map_final.csv'
# csv file; all rows have less than 4 NaN values, organized by patient ID and time; data includes 6 vitals + map

df = pd.read_csv('chart_events_map_final.csv')

hour_mark = '00:00'

to_drop = []

for i in range(len(df)):
    if df['CHARTTIME'][i].endswith(hour_mark):
        pass

    else:
        to_drop.append(i)
        # df = df.drop(i, axis=0)

df = df.drop(df.index[to_drop])
df = df.reset_index(drop=True)
df.to_csv('chart_events_by_hour.csv', index=False)





# now have data from exact hours
# now need to sample 7 hours of data for each patient

# pseudocode:
# check if each patient has 6+ datapoints
# for each unique patient
# drop all but 7 datapoints

# transpose table so that each row contains 6 x 7 cols
# get rid of charttime

# newdf = []
#
# for i in range(len(newdf.unique())):
#     pass

# date_time = datetime.strptime(df.loc[1][1], '%Y-%m-%d %H:%M:%S')
# date_time2 = datetime.strptime(df.loc[7][1], '%Y-%m-%d %H:%M:%S')
# print(date_time2 - date_time)
# print(df.loc[df['map'] < 65].index)

