import pandas as pd

# input: 1 csv file containing vital sign information only, output: 1 csv file containing
# patients with at least 36 data points (1 per hour for 6 hours, 6 vital signs), sorted by ascending patient ID


def csv_file_sort_and_clean():

    chart_events = pd.read_csv('chart_events.csv').sort_values(['SUBJECT_ID', 'CHARTTIME'], ascending=True)
    chart_events = chart_events.drop(['STORETIME', 'VALUENUM'], axis=1)
    # rationale: at least 6 vital sign records for each hour for 6 hours; hence a patient should contain > 35 rows
    chart_events = chart_events.groupby("SUBJECT_ID").filter(lambda x: len(x) > 35)

    chart_events.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)

    chart_events.to_csv('chart_events_sorted.csv', index=False)
    chart_events.to_pickle('chart_events_sorted.pkl')


# output as of now is a single csv file, sorted by patient ID, containing vital sign information; each patient
# appears at least 36 times
# csv_file_sort_and_clean()

