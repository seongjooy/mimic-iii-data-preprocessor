import pandas as pd
import os
import gzip
import vitals_id

# this extractor takes the raw MIMIC III input data and outputs 221 csv files, where output columns only consist of
# vital sign data of the patients (BT, SBP, DBP, RR, SP02, HR)

if __name__ == '__main__':

    def vitals_extractor():
        csv_list = []
        chart_events_csv = gzip.open('CHARTEVENTS.csv.gz', 'rt', newline='')
        chunk_size = 1500000
        batch_no = 1
        # splitting CSV files:
        for chunk in pd.read_csv(chart_events_csv, chunksize=chunk_size):

            # drop meaningless columns first to reduce memory (reduced by about 33%)
            chunk.drop(['ROW_ID', 'HADM_ID', 'ICUSTAY_ID', 'CGID', 'WARNING', 'ERROR', 'RESULTSTATUS', 'STOPPED'],
                          axis='columns', inplace=True)
            chunk = chunk.loc[chunk['ITEMID'].isin(vitals_id.VITALS_ID)]
            # save as new csv
            chunk.to_csv('chartEvents_' + str(batch_no) + '.csv', index=False)

            # print batch number with file size for visualization
            print('batch_no = ' + str(batch_no) + '\n' + 'filesize = ' +
                  str(os.path.getsize('chartEvents_' + str(batch_no) + '.csv')) + 'bytes')
            batch_no += 1
        # end of splitting CSV files # output: 221 .csv files


        # extracting rows with valid vital sign IDs: # output: 221 .csv files
        # (~40 MB each, ~63 bytes each for 172th file onwards)

        merged_csv = pd.concat(
            map(pd.read_csv, csv_list), ignore_index=True
        )

        csv_list = []

        for i in range(221):
            csv_list.append('chartEvents_' + str(i+1) + '.csv')
            print(i+1)

        merged_csv = pd.concat(
            map(pd.read_csv, csv_list), ignore_index=True
        )

        merged_csv.to_csv('chart_events.csv')

vitals_extractor()
