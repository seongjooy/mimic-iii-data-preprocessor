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


