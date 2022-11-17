import pandas as pd
import matplotlib.pyplot as plt

DATA = "./data/DAVIS_2021and22.txt"
KEY = "Bar  "
DATE = "Date"
TIME = "Time"
CREATE_DATE = "CREATEDATE"


def clean_dataset(dataframe):
    dataframe[CREATE_DATE] = dataframe[DATE].astype(str) + " " + dataframe[TIME]
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    print(dataframe)
    return dataframe[[CREATE_DATE, KEY]]


def get_mean_value(dataframe):
    dataframe["MEAN_30"] = dataframe[KEY].groupby(dataframe[KEY].index // 30).mean()
    return dataframe


def get_pressure_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=1))
    data = clean_dataset(data)
    data = pd.DataFrame(data)
    return data


if __name__ == '__main__':
    df = get_pressure_dataframe(DATA)
    plt.scatter(df[CREATE_DATE], df[KEY])
    plt.ylabel("Pressure (HPA)")
    plt.show()
    df.to_excel("./DAVIS_PRESSURE.xlsx")
