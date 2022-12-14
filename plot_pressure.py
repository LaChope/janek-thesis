# imports are just external libraries to use code already writen by other people

import glob
import matplotlib.pyplot as plt
import pandas as pd

from lkpr_scripts import LKPR_pressure
from davis_scripts import DAVIS_pressure

# Defines all the constants used from the table
BARO_DATA_LKPR = glob.glob("./data/*/*/BARO/*.his")
KEY1 = "PA_QNH (HPA)"

BARO_DATA_DAVIS = "./data/DAVIS_2021and22.txt"
KEY2 = "Bar  "
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


# Get the dataframe from the other script "LKPR/DAVIS_pressure.py" used to be plotted
davis_df = DAVIS_pressure.get_full_dataframe()
lkpr_df = LKPR_pressure.get_full_dataframe()

lkpr_df.rename(columns={KEY1: KEY2}, inplace=True)

inner_merge = pd.merge(davis_df, lkpr_df, on=[CREATE_DATE])
inner_merge["Difference"] = inner_merge[KEY2 + "_x"] - inner_merge[KEY2 + "_y"]

# Define how the data should be plotted
fig, (a, b) = plt.subplots(2, 1, sharex=True)
a.scatter(lkpr_df[CREATE_DATE], lkpr_df[KEY2], label="LKPR")
a.scatter(davis_df[CREATE_DATE], davis_df[KEY2], label="DAVIS")
a.set_title("LKPR / DAVIS Pressure")

b.bar(inner_merge[CREATE_DATE], inner_merge["Difference"], width=0.01)
b.set_title("Difference")
a.legend(loc='upper left')

a.set_ylabel(KEY1)
b.set_ylabel(KEY1)
plt.show()


