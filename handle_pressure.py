import pandas as pd


def clean_dataset(dataframe):
    dataframe.columns = dataframe.iloc[1]
    dataframe = dataframe.iloc[2:, :]
    dataframe["PA_QNH (HPA)"] = dataframe["PA_QNH (HPA)"].str.replace(',', '.').astype("float")
    return dataframe


def get_mean_value(dataframe):
    return dataframe["PA_QNH (HPA)"].groupby(dataframe["PA_QNH (HPA)"].index // 30).mean()


def get_pressure_dataframe(file):
    df = pd.DataFrame(pd.read_excel(file))
    df = clean_dataset(df)
    df = get_mean_value(df)
    df = pd.DataFrame(df)
    df.insert(0, "Time (h)", (df.index * 30) / 60)
    return df


