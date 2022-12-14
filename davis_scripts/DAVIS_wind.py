import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate

DATA = "./data/DAVIS_2021and22.txt"
KEY = "Wind"
DATE = "Unnamed: 0"
TIME = "Unnamed: 1"
CREATE_DATE = "CREATEDATE"
WIND_DIRECTION = "Wind.1"

COMPASS={'N':0, 'NNE':22.5,"NE":45,"ENE":67.5, 'E':90,'ESE':112.5, 'SE':135,'SSE':157.5, 'S':180,'SSW':202.5, 'SW':225,'WSW':247.5, 'W':270,'WNW':292.5,'NW':315,'NNW':337.5}




def clean_dataset(dataframe):
    dataframe[CREATE_DATE] = dataframe[DATE].astype(str) + " " + dataframe[TIME]
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    dataframe[KEY] = pd.to_numeric(dataframe[KEY])
    dataframe = dataframe[dataframe[KEY].apply(lambda x: isinstance(x, (float, np.float32)))]
    dataframe[WIND_DIRECTION] = dataframe[WIND_DIRECTION].str.strip().replace(COMPASS)
    dataframe[WIND_DIRECTION] = pd.to_numeric(dataframe[WIND_DIRECTION], errors="coerce").dropna()
    # print(dataframe[WIND_DIRECTION])
    return dataframe[[CREATE_DATE, KEY, WIND_DIRECTION]]


def get_wind_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=range(1, 2)))
    data = clean_dataset(data)
    data = pd.DataFrame(data)
    return data



def get_full_dataframe():
    return get_wind_dataframe(DATA)
    # fig, (a, b) = plt.subplots(2, 1, sharex=True)
    # df = get_wind_dataframe(DATA)
    # a.scatter(df[CREATE_DATE], df[KEY])
    # a.set_ylabel('Wind velocity (KT)')
    # plt.ylabel("Wind (KT)")

    # print(df[WIND_DIRECTION])

    # b.bar(df[CREATE_DATE], df[WIND_DIRECTION], width=0.01)
    # b.set_ylabel('Wind direction (degrees)')
    # plt.show()
    # df.to_excel("./DAVIS_PRESSURE.xlsx")

# get_full_dataframe()
