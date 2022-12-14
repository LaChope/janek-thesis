import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate

DATA = "./data/DAVIS_2021and22.txt"
KEY = "Wind"
DATE = "Unnamed: 0"
TIME = "Unnamed: 1"
CREATE_DATE = "CREATEDATE"


def clean_dataset(dataframe):
    dataframe[CREATE_DATE] = dataframe[DATE].astype(str) + " " + dataframe[TIME]
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    # dataframe[KEY] = dataframe[KEY].str.replace(r'\---', '0').astype(float)
    dataframe[KEY] = pd.to_numeric(dataframe[KEY])
    dataframe = dataframe[dataframe[KEY].apply(lambda x: isinstance(x, (float, np.float32)))]
    return dataframe[[CREATE_DATE, KEY]]


def get_wind_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=range(1, 2)))
    data = clean_dataset(data)
    data = pd.DataFrame(data)
    return data


def get_full_dataframe():
    return get_wind_dataframe(DATA)
    # df = get_wind_dataframe(DATA)
    # plt.scatter(df[CREATE_DATE], df[KEY])
    # plt.ylabel("Wind (KT)")
    # plt.show()
    # df.to_excel("./DAVIS_PRESSURE.xlsx")

# get_full_dataframe()
