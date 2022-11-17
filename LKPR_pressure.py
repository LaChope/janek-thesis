import pandas as pd
import glob
import matplotlib.pyplot as plt

baro_data = glob.glob("./data/2021/*/BARO/PRESSURE_1_*.his")


def clean_dataset(dataframe):
    dataframe["CREATEDATE"] = pd.to_datetime(dataframe["CREATEDATE"], infer_datetime_format=True)
    return dataframe[["CREATEDATE", "PA_QNH (HPA)"]]


def get_mean_value(dataframe):
    dataframe["MEAN_30"] = dataframe["PA_QNH (HPA)"].groupby(dataframe["PA_QNH (HPA)"].index // 30).mean()
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
        df = get_pressure_dataframe(str(baro_data[i]))
        df_list.append(df)
    concat_df = pd.concat(df_list)
    plt.scatter(concat_df["CREATEDATE"], concat_df["PA_QNH (HPA)"])
    plt.xlabel("Date")
    plt.ylabel("Pressure (HPA)")
    plt.show()
    concat_df.to_excel("./PRESSURE.xlsx")
