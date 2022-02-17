# file contains relevant vital IDs for shock analysis:

# respiratory rate
RR_ID = [615, 618, 220210, 224690]
# heart rate
HR_ID = [211, 220045]
# systolic BP
SBP_ID = [51, 442, 455, 6701, 220179, 220050]
# diastolic BP
DBP_ID = [8368, 8440, 8441, 8555, 220180, 220051]
# body temperature
BT_ID = [678, 223761]
# oxygen saturation
SPO2_ID = [220227, 220277, 646]

VITALS_ID = RR_ID + HR_ID + SBP_ID + DBP_ID + BT_ID + SPO2_ID

# need to compute MBP from SBP and DBP, then use in shock analysis
