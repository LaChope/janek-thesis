import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


WIND_DATA_06 = glob.glob("./data/*/*/WIND06/*.his")
WIND_DATA_12 = glob.glob("./data/*/*/WIND12/*.his")
KEY = "WSINS (KT)"
KEY2 = "WSINS(M/S)"
WIND_DIRECTION="WDINS"
CREATE_DATE = "CREATEDATE"


def clean_dataset(dataframe):
    dataframe = get_mean_value(dataframe)
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    dataframe[WIND_DIRECTION] = pd.to_numeric(dataframe[WIND_DIRECTION], errors="coerce").dropna()
    radians = np.deg2rad(dataframe[WIND_DIRECTION])
    rounded = np.rad2deg(np.round(radians / (np.pi/2)) * (np.pi/2))
    dataframe[WIND_DIRECTION] = rounded
    if KEY in dataframe:
        dataframe = dataframe[dataframe[KEY].apply(lambda x: isinstance(x, (float, np.float32)))]
        return dataframe[[CREATE_DATE, KEY, WIND_DIRECTION]]
    if KEY2 in dataframe:
        dataframe = dataframe[dataframe[KEY2].apply(lambda x: isinstance(x, (float, np.float32)))]
        dataframe[KEY] = dataframe[KEY2].values * 1.9
        return dataframe[[CREATE_DATE, KEY, WIND_DIRECTION]]

def get_mean_value(dataframe):
    # dataframe["MEAN_30"] = dataframe[KEY].groupby(dataframe[KEY].index // 30).mean()
    # return dataframe

    dataframe = dataframe.iloc[::30, :]
    return dataframe


def get_wind_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=1))
    data = clean_dataset(data)
    data = pd.DataFrame(data)
    return data


def get_full_dataframe():
    df_list_06 = []
    df_list_12 = []
    for i in range(len(WIND_DATA_06)):
        df = get_wind_dataframe(str(WIND_DATA_06[i]))
        df_list_06.append(df)

    for i in range(len(WIND_DATA_12)):
        df = get_wind_dataframe(str(WIND_DATA_12[i]))
        df_list_12.append(df)

    return [pd.concat(df_list_06), pd.concat(df_list_12)]
    # concat_df_06 = pd.concat(df_list_06)
    # concat_df_12 = pd.concat(df_list_12)
    #
    # fig, ax = plt.subplots(2, 2, sharex=True)
    # ax[0][0].scatter(concat_df_06[CREATE_DATE], concat_df_06[KEY], label="LKPR 06")
    # ax[0][0].set_ylabel('Wind velocity (KT)')
    #
    # ax[1][0].bar(concat_df_06[CREATE_DATE], concat_df_06[WIND_DIRECTION], width=0.01)
    # ax[1][0].set_ylabel('Wind direction (degrees)')
    #
    # ax[0][1].scatter(concat_df_12[CREATE_DATE], concat_df_12[KEY], label="LKPR 12")
    # ax[0][1].set_ylabel('Wind velocity (KT)')
    #
    # ax[1][1].bar(concat_df_12[CREATE_DATE], concat_df_12[WIND_DIRECTION], width=0.01)
    # ax[1][1].set_ylabel('Wind direction (degrees)')
    # plt.show()

# get_full_dataframe()
