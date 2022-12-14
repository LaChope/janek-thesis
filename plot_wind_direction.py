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
LKPR_WIND_DIRECTION= "WDINS"

DAVIS_DATA = "./data/DAVIS_2021and22.txt"
DAVIS_KEY = "Wind"
DAVIS_DATE = "Unnamed: 0"
DAVIS_TIME = "Unnamed: 1"
DAVIS_CREATE_DATE = "CREATEDATE"
DAVIS_WIND_DIRECTION = "Wind.1"

davis_df = DAVIS_wind.get_full_dataframe()
lkpr_df_06 = LKPR_wind.get_full_dataframe()[0]
lkpr_df_12 = LKPR_wind.get_full_dataframe()[1]

fig, ax = plt.subplots(2, 3, sharex=True)
ax[0][0].scatter(lkpr_df_06[CREATE_DATE], lkpr_df_06[LKPR_KEY])
ax[0][0].set_title("LKPR 06 Wind Speed")
ax[0][0].set_ylabel('Wind velocity (KT)')

ax[1][0].bar(lkpr_df_06[CREATE_DATE], lkpr_df_06[LKPR_WIND_DIRECTION], width=0.01)
ax[1][0].set_ylabel('Wind direction (degrees)')

ax[0][1].scatter(lkpr_df_12[CREATE_DATE], lkpr_df_12[LKPR_KEY])
ax[0][1].set_title("LKPR 12 Wind Speed")
ax[0][1].set_ylabel('Wind velocity (KT)')

ax[1][1].bar(lkpr_df_12[CREATE_DATE], lkpr_df_12[LKPR_WIND_DIRECTION], width=0.01)
ax[1][1].set_ylabel('Wind direction (degrees)')

ax[0][2].scatter(davis_df[CREATE_DATE], davis_df[DAVIS_KEY])
ax[0][2].set_title("DAVIS Wind Speed")
ax[0][2].set_ylabel('Wind velocity (KT)')

ax[1][2].bar(davis_df[CREATE_DATE], davis_df[DAVIS_WIND_DIRECTION], width=0.01)
ax[1][2].set_ylabel('Wind direction (degrees)')

plt.show()
