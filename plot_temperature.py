import glob
import pandas as pd
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

lkpr_df.rename(columns={KEY1: KEY2}, inplace=True)

inner_merge = pd.merge(davis_df, lkpr_df, on=[CREATE_DATE])
inner_merge["Difference"] = inner_merge[KEY2 + "_x"] - inner_merge[KEY2 + "_y"]

# Define how the data should be plotted
fig, (a, b) = plt.subplots(2, 1, sharex=True)
a.scatter(lkpr_df[CREATE_DATE], lkpr_df[KEY2], label="LKPR")
a.scatter(davis_df[CREATE_DATE], davis_df[KEY2], label="DAVIS")
a.set_title("LKPR / DAVIS")

b.bar(inner_merge[CREATE_DATE], inner_merge["Difference"])
b.set_title("Difference")
a.legend(loc='upper left')

a.set_ylabel(KEY1)
b.set_ylabel(KEY1)
plt.show()


