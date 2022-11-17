import pandas as pd
import glob
import matplotlib.pyplot as plt

TEMP_DATA = glob.glob("./data/2021/*/TEMP/TEMP_MET_01*.his")
KEY = "THT_TT"
CREATE_DATE = "CREATEDATE"



def clean_dataset(dataframe):
    dataframe[CREATE_DATE] = pd.to_datetime(dataframe[CREATE_DATE], infer_datetime_format=True)
    return dataframe[[CREATE_DATE, KEY]]


def get_mean_value(dataframe, key):
    dataframe["MEAN_30"] = dataframe[key].groupby(dataframe[key].index // 30).mean()
    return dataframe


def get_pressure_dataframe(file):
    data = pd.DataFrame(pd.read_csv(file, delimiter='\t', engine="python", skiprows=1))
    data = clean_dataset(data, KEY)
    # df = get_mean_value(df)
    data = pd.DataFrame(data)
    # df.insert(0, "Time (h)", (df.index * 30) / 60)
    return data


if __name__ == '__main__':
    df_list = []
    for i in range(len(TEMP_DATA)):
    # for i in range(2):
        df = get_pressure_dataframe(str(TEMP_DATA[i]))
        df_list.append(df)
    concat_df = pd.concat(df_list)
    plt.scatter(concat_df[CREATE_DATE], concat_df[KEY])
    plt.ylabel("Temp")
    plt.show()
    # concat_df.to_excel("./TEMPERATURE.xlsx")
