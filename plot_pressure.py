import glob
import matplotlib.pyplot as plt
import LKPR_pressure
import DAVIS_pressure

BARO_DATA = glob.glob("./data/*/*/BARO/*.his")
KEY1 = "PA_QNH (HPA)"

DATA = "./data/DAVIS_2021and22.txt"
KEY2 = "Bar  "
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


davis_df = DAVIS_pressure.get_full_dataframe()
lkpr_df = LKPR_pressure.get_full_dataframe()

plt.scatter(lkpr_df[CREATE_DATE], lkpr_df[KEY1])
plt.scatter(davis_df[CREATE_DATE], davis_df[KEY2])

plt.ylabel(KEY1)
plt.show()


