import pandas as pd

if __name__ == '__main__':
    # CONVERTING CHARTEVENTS TO INPUT FORM, AND ADDING MAP VALUE
    df = pd.read_csv('chart_events.csv')
    df = df.drop(['VALUEUOM'], axis=1)

    df = df.pivot_table(values='VALUE', index=['SUBJECT_ID',
                                               'CHARTTIME'], columns='ITEMID', aggfunc='first')

    # df.reset_index(inplace=True, drop=False)
    # df.reset_index(level=['SUBJECT_ID', 'CHARTTIME'])
    df.columns.name = None
    df = df.reset_index(drop=False)

    df['map'] = (2 * df['dbp'] + df['sbp']) / 3

    df.to_csv('chart_events_map.csv', index=False)

    # df = pd.read_csv('chart_events_map.csv')
    # total of 8,618,649 rows
    # total of 809,239 rows with map score < 65

    # keep rows where there are less than 4 NaN values // delete rows with 4+ NaN values
    df = df[df.isnull().sum(axis=1) < 4]
    # total of 5,579,366 rows
    # total of 769,900 rows with map score < 65
    # saved as chart_events_map_final.csv
