import glob
import matplotlib.pyplot as plt
from lkpr_scripts import LKPR_pressure
from davis_scripts import DAVIS_pressure

BARO_DATA_LKPR = glob.glob("./data/*/*/BARO/*.his")
KEY1 = "PA_QNH (HPA)"

BARO_DATA_DAVIS = "./data/DAVIS_2021and22.txt"
KEY2 = "Bar  "
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


#df = dataframe
davis_df = DAVIS_pressure.get_full_dataframe()
lkpr_df = LKPR_pressure.get_full_dataframe()

plt.scatter(lkpr_df[CREATE_DATE], lkpr_df[KEY1], label="LKPR")
plt.scatter(davis_df[CREATE_DATE], davis_df[KEY2], label="DAVIS")
plt.legend(loc='upper left')


plt.ylabel(KEY1)
plt.show()


