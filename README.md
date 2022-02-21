# Extracting Vital Sign Data from the MIMIC-III Dataset
Purpose: Extracting vital sign data of patients from the raw MIMIC-III dataset, into a usable format for training an XGBoost model for predicting the onset of septic shock (base for: https://github.com/seongjooy/septic-shock-predictor). <br/> <br/>
The dataset can be found at: https://physionet.org/content/mimiciii/1.4/. <br/> <br/>

**Input**: Raw MIMIC-III data file, .csv.gz, consisting of de-identified patient chart event information. <br/>
**Final Output**: Processed .csv file, consisting of only the vital sign data of the patients that are also consecutive for at least 6 hours. <br/><br/>

**File Descriptions:** <br/>

'vitals_id.py'<br/>
**Input**: None   <br/>
**Output**: None   <br/>
Data from MIMIC-III has columns that are not explicitly labelled (ex. 'Heart Rate'), but instead are number-coded (ex. '210500') which correspond to each element. Hence, to filter vital signs, their respective IDs were mapped from 'D_ITEMS.csv', the MIMIC-III source file, and the required number-codes saved here in 'vitals_id.py'.


'vitals_extractor.py'<br/>
**Input**: CHARTEVENTS.csv.gz – zip file containing comprehensive information of patients <br/>
**Output**: chart_events.csv – zip file containing only vital sign information of patients <br/>
First unzips the data file. Filters the zip file containing all the chartevents of patients to just the vital sign information of patients. Filtering is done with help from the 'vitals_id.py' file, used to identify which columns to keep or drop.

'csv_file_process.py'<br/>
**Input**: 'chart_events.csv' – from previous step <br/>
**Output**: 'chart_events_sorted.csv' – .csv file containing vital sign info that are consecutive for at least 6 hours <br/>
Patient vital sign data is not guaranteed to last for at least 6 hours, which is a requirement for the study to be done. Therefore, this file drops all patient cases where the vital sign data does not last for a minimum of 6 hours.

'csv_pivot_and_reformat.py'<br/>
**Input**: 'chart_events_sorted.csv' – from previous step <br/>
**Output**: 'chart_events_final.csv' –  <br/>
The data table is not compatible with the AI model to be utilized. Hence, the table is pivotted in a way so that it can be directly input to the AI model. Further, an additional feature is generated which is tested and proved to improve the performance of the model.

'main.py'<br/>
**Input**: 'chart_events_final.csv' – from previous step <br/>
**Output**: 'chart_events_by_hour.csv' –  <br/>
At this point, the .csv file contains patient information on vital signs, guaranteed to be consecutive for at least 6 hours. However, data from MIMIC-III is recorded in intervals of 15 minutes. Since the model requires data in 1-hour intervals (ie. 10:15, 11:15, 12:15, ... , 15:15), data should be grouped by their minute-hand times. A total of 4 files can be generated (:00, :15, :30, :45), of which 6 hours of data can be extracted from each file as one valid train case. 


'sample_chart.py'<br/>
**Input**: 'chart_events_final.pkl' –  <br/>
**Output**: 'chart_events_sampled.csv' <br/>
Not used in the process – an intermediate file to test methods on a smaller scale; sample_chart.py reduces the final pre-processed data table to 1000 patients, allowing for quicker unit testing.
