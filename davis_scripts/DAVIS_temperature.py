# import are libraries/packages = code from other people

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate

DATA = "./data/DAVIS_2021and22.txt"
KEY = "Temp"
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


def clean_dataset(dataframe):
    dataframe[CREATE_DATE] = dataframe[DATE].astype(str) + " " + dataframe[TIME]
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    dataframe[KEY] = dataframe[KEY].str.replace(r'\---', '0').astype(float)
    dataframe[KEY] = pd.to_numeric(dataframe[KEY])
    dataframe = dataframe[dataframe[KEY].apply(lambda x: isinstance(x, (float, np.float32)))]
    return dataframe[[CREATE_DATE, KEY]]


def get_temperature_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=1))
    data = clean_dataset(data)
    data = pd.DataFrame(data)
    return data


def get_full_dataframe():
    # return get_temperature_dataframe(DATA)
    df = get_temperature_dataframe(DATA)
    plt.scatter(df[CREATE_DATE], df[KEY])
    plt.ylabel("Temp")
    plt.show()
    df.to_excel("./DAVIS_TEMPERATURE.xlsx")


get_full_dataframe()
