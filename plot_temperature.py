import glob
import matplotlib.pyplot as plt
import DAVIS_temperature
import LKPR_temperature

TEMP_DATA = glob.glob("./data/*/*/TEMP/*.his")
KEY1 = "TH_TT"


DATA = "./data/DAVIS_2021and22.txt"
KEY2 = "Temp"
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


davis_df = DAVIS_temperature.get_full_dataframe()
lkpr_df = LKPR_temperature.get_full_dataframe()

plt.scatter(lkpr_df[CREATE_DATE], lkpr_df[KEY1])
plt.scatter(davis_df[CREATE_DATE], davis_df[KEY2])

plt.ylabel(KEY1)
plt.show()


