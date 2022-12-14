import glob
import pandas as pd
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
DAVIS_CREATE_DATE = "CREATEDATE"

davis_df = DAVIS_wind.get_full_dataframe()
lkpr_df_06 = LKPR_wind.get_full_dataframe()[0]
lkpr_df_12 = LKPR_wind.get_full_dataframe()[1]

lkpr_df_06.rename(columns={LKPR_KEY: DAVIS_KEY}, inplace=True)
lkpr_df_12.rename(columns={LKPR_KEY: DAVIS_KEY}, inplace=True)

inner_merge_06 = pd.merge(davis_df, lkpr_df_06, on=[CREATE_DATE])
inner_merge_06["Difference"] = inner_merge_06[DAVIS_KEY + "_x"] - inner_merge_06[DAVIS_KEY + "_y"]

inner_merge_12 = pd.merge(davis_df, lkpr_df_12, on=[CREATE_DATE])
inner_merge_12["Difference"] = inner_merge_12[DAVIS_KEY + "_x"] - inner_merge_12[DAVIS_KEY + "_y"]

# Define how the data should be plotted
fig, ax = plt.subplots(2, 2, sharex=True)
ax[0][0].scatter(lkpr_df_06[CREATE_DATE], lkpr_df_06[DAVIS_KEY], label="LKPR 06")
ax[0][0].scatter(davis_df[CREATE_DATE], davis_df[DAVIS_KEY], label="DAVIS")
ax[0][0].set_title("LKPR 06 / DAVIS")
ax[0][0].legend(loc='upper left')

ax[1][0].bar(inner_merge_06[CREATE_DATE], inner_merge_06["Difference"])
ax[1][0].set_title("Difference")

ax[0][1].scatter(lkpr_df_12[CREATE_DATE], lkpr_df_12[DAVIS_KEY], label="LKPR 12")
ax[0][1].scatter(davis_df[CREATE_DATE], davis_df[DAVIS_KEY], label="DAVIS")
ax[0][1].set_title("LKPR 12 / DAVIS")
ax[0][1].legend(loc='upper left')

ax[1][1].bar(inner_merge_12[CREATE_DATE], inner_merge_12["Difference"])
ax[1][1].set_title("Difference")


ax[0][0].set_ylabel(LKPR_KEY)
ax[0][1].set_ylabel(LKPR_KEY)
ax[1][0].set_ylabel(LKPR_KEY)
ax[1][1].set_ylabel(LKPR_KEY)
plt.show()

# plt.scatter(davis_df[CREATE_DATE], davis_df[DAVIS_KEY], label="DAVIS")
#
# plt.scatter(lkpr_df[0][CREATE_DATE], lkpr_df[0][LKPR_KEY], label="LKPR Site 06")
# plt.scatter(lkpr_df[1][CREATE_DATE], lkpr_df[1][LKPR_KEY], label="LKPR Site 12")
# plt.legend(loc='upper left')
# plt.ylabel(LKPR_KEY)
# plt.show()



