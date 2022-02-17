import pandas as pd
import random
# goal: sample 1000 unique patients based on ID and create a dataframe


# df = pd.read_csv('chart_events.csv')
# df.to_pickle('chart_events_final.pkl')

def sample_chart():

    df = pd.read_pickle('chart_events_final.pkl')

    # length 1000
    rand_patients_test = random.sample(df['SUBJECT_ID'].unique().tolist(), 1000)

    df_sample = df.loc[df['SUBJECT_ID'].isin(rand_patients_test)]

    print(len(df_sample))
    print(len(df_sample['SUBJECT_ID'].unique()))

    df_sample.to_csv('chart_events_sampled.csv', index=False)

# output is chart_events_sampled.csv, this has 1000 patients randomly sampled
# df = pd.read_pickle('chart_events_sampled.csv')
# df.to_pickle('chart_events_sampled_sorted.pkl')

# sample_chart()
