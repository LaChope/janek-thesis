import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


WIND_DATA_06 = glob.glob("./data/*/*/WIND06/*.his")
WIND_DATA_12 = glob.glob("./data/*/*/WIND12/*.his")
KEY = "WSINS (KT)"
KEY2 = "WSINS(M/S)"
CREATE_DATE = "CREATEDATE"


def clean_dataset(dataframe):
    dataframe = get_mean_value(dataframe)
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    if KEY in dataframe:
        dataframe = dataframe[dataframe[KEY].apply(lambda x: isinstance(x, (float, np.float32)))]
        return dataframe[[CREATE_DATE, KEY]]
    if KEY2 in dataframe:
        dataframe = dataframe[dataframe[KEY2].apply(lambda x: isinstance(x, (float, np.float32)))]
        dataframe[KEY] = dataframe[KEY2].values * 1.9
        return dataframe[[CREATE_DATE, KEY]]

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
    # plt.scatter(concat_df_06[CREATE_DATE], concat_df_06[KEY], label="Site 06")
    # plt.scatter(concat_df_12[CREATE_DATE], concat_df_12[KEY], label="Site 12")
    # plt.legend(loc='upper left')
    # plt.ylabel(KEY)
    # plt.show()
    # concat_df_06.to_excel("./LKPR_WIND.xlsx")


# get_full_dataframe()
