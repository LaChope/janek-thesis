import glob
import matplotlib.pyplot as plt
from lkpr_scripts import LKPR_wind
from davis_scripts import DAVIS_wind

LKPR_WIND_DATA_06 = glob.glob("./data/*/*/WIND06/*.his")
LKPR_WIND_DATA_12 = glob.glob("./data/*/*/WIND12/*.his")
LKPR_KEY = "WSINS (KT)"
LKPR_KEY2 = "WSINS(M/S)"
CREATE_DATE = "CREATEDATE"

DAVIS_DATA = "./data/DAVIS_2021and22.txt"
DAVIS_KEY = "Wind"
DAVIS_DATE = "Unnamed: 0"
DAVIS_TIME = "Unnamed: 1"
DAVISCREATE_DATE = "CREATEDATE"



davis_df = DAVIS_wind.get_full_dataframe()
lkpr_df = LKPR_wind.get_full_dataframe()

plt.scatter(davis_df[CREATE_DATE], davis_df[DAVIS_KEY], label="DAVIS")

plt.scatter(lkpr_df[0][CREATE_DATE], lkpr_df[0][LKPR_KEY], label="LKPR Site 06")
plt.scatter(lkpr_df[1][CREATE_DATE], lkpr_df[1][LKPR_KEY], label="LKPR Site 12")
plt.legend(loc='upper left')
plt.ylabel(LKPR_KEY)
plt.show()



