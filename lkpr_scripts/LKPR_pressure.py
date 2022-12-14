import pandas as pd
import numpy as np
import glob

from matplotlib import pyplot as plt

BARO_DATA = glob.glob("./data/*/*/BARO/*.his")
KEY = "PA_QNH (HPA)"
CREATE_DATE = "CREATEDATE"

# Clean the dataset by removing unused columns, and putting the date column into a format python understands
def clean_dataset(dataframe):
    dataframe = get_mean_value(dataframe)
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    dataframe = dataframe[dataframe[KEY].apply(lambda x: isinstance(x, (float, np.float32)))]
    return dataframe[[CREATE_DATE, KEY]]

# Keep only value every 30 rows
def get_mean_value(dataframe):
    # dataframe["MEAN_30"] = dataframe[KEY].groupby(dataframe[KEY].index // 30).mean()
    # return dataframe

    dataframe = dataframe.iloc[::30, :]
    return dataframe

# Get the correct files containing pressure only
def get_pressure_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=1))
    data = clean_dataset(data)
    data = pd.DataFrame(data)
    return data


# Create the final dataframe
def get_full_dataframe():
    df_list = []
    for i in range(len(BARO_DATA)):
        df = get_pressure_dataframe(str(BARO_DATA[i]))
        df_list.append(df)
    return pd.concat(df_list)
    # concat_df = pd.concat(df_list)
    # plt.scatter(concat_df[CREATE_DATE], concat_df[KEY])
    # plt.ylabel(KEY)
    # plt.show()
    # concat_df.to_excel("./LKPR_PRESSURE.xlsx")

# get_full_dataframe()