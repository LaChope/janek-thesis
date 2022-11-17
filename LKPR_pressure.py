import pandas as pd
import glob
import matplotlib.pyplot as plt

BARO_DATA = glob.glob("./data/2021/*/BARO/PRESSURE_1_*.his")
KEY = "PA_QNH (HPA)"
CREATE_DATE = "CREATEDATE"


def clean_dataset(dataframe):
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    return dataframe[[CREATE_DATE, KEY]]


def get_mean_value(dataframe):
    dataframe["MEAN_30"] = dataframe[KEY].groupby(dataframe[KEY].index // 30).mean()
    return dataframe


def get_pressure_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=1))
    data = clean_dataset(data)
    # df = get_mean_value(df)
    data = pd.DataFrame(data)
    # df.insert(0, "Time (h)", (df.index * 30) / 60)
    return data


if __name__ == '__main__':
    df_list = []
    # for i in range(len(baro_data)):
    for i in range(2):
        df = get_pressure_dataframe(str(BARO_DATA[i]))
        df_list.append(df)
    concat_df = pd.concat(df_list)
    plt.scatter(concat_df[CREATE_DATE], concat_df[KEY])
    plt.ylabel("Pressure (HPA)")
    plt.show()
    concat_df.to_excel("./PRESSURE.xlsx")
