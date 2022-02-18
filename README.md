# Extracting Vital Sign Data from the MIMIC-III Dataset
Purpose: Extracting vital sign data of patients from the raw MIMIC-III dataset, into a usable format for training an XGBoost model for predicting the onset of septic shock (https://github.com/seongjooy/septic-shock-predictor). <br/> <br/>
The dataset can be found at: https://physionet.org/content/mimiciii/1.4/. <br/> <br/>

**Input**: Raw MIMIC-III data file, .csv.gz, consisting of de-identified patient chart event information. <br/>
**Final Output**: Processed .csv file, consisting of only the vital sign data of the patients that are also consecutive for at least 6 hours. <br/><br/>

**File Descriptions:** <br/>

'vitals_id.py'<br/>
**Input**: None   <br/>
**Output**: None   <br/>
Data from MIMIC-III has columns that are not explicitly labelled (ex. 'Heart Rate'), but instead are number-coded (ex. '210500') which correspond to each element. Hence, to filter vital signs, their respective IDs were mapped from 'D_ITEMS.csv' and the required number-codes saved here in 'vitals_id.py'.


'vitals_extractor.py'<br/>
**Input**: CHARTEVENTS.csv.gz – zip file containing comprehensive information of patients <br/>
**Output**: chart_events.csv – zip file containing only vital sign information of patients <br/>
Description

'csv_file_process.py'<br/>
**Input**: 'chart_events.csv' – from previous step <br/>
**Output**: 'chart_events_sorted.csv' – .csv file containing vital sign info that are consecutive for at least 6 hours <br/>
Description

'csv_pivot_and_reformat.py'<br/>
**Input**: 'chart_events_sorted.csv' – from previous step <br/>
**Output**: 'chart_events_final.csv' –  <br/>
Description

'main.py'<br/>
**Input**: 'chart_events_final.csv' – from previous step <br/>
**Output**: 'chart_events_by_hour.csv' –  <br/>
Description


'sample_chart.py'<br/>
**Input**: 'chart_events_final.pkl' –  <br/>
**Output**: 'chart_events_sampled.csv' <br/>
Description
