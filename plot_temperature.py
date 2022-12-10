import glob
import matplotlib.pyplot as plt
from davis_scripts import DAVIS_temperature
from lkpr_scripts import LKPR_temperature

TEMP_DATA_LKPR = glob.glob("./data/*/*/TEMP/*.his")
KEY1 = "TH_TT"

TEMP_DATA_DAVIS = "./data/DAVIS_2021and22.txt"
KEY2 = "Temp"
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


davis_df = DAVIS_temperature.get_full_dataframe()
lkpr_df = LKPR_temperature.get_full_dataframe()

plt.scatter(lkpr_df[CREATE_DATE], lkpr_df[KEY1], label="LKPR")
plt.scatter(davis_df[CREATE_DATE], davis_df[KEY2], label="DAVIS")
plt.legend(loc='upper left')

plt.ylabel(KEY1)
plt.show()


