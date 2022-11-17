import pandas as pd

df = pd.DataFrame(pd.read_excel("data/2021/7-červenec 21/BARO/PRESSURE_1_01.xlsx"))
df.columns = df.iloc[1]
df = df.iloc[2:, :]
df["PA_QNH (HPA)"] = df["PA_QNH (HPA)"].str.replace(',', '.').astype("float")

meanDf = df["PA_QNH (HPA)"].groupby(df["PA_QNH (HPA)"].index // 30).mean()
print(meanDf)
meanDf.to_excel("./Test.xlsx", index=False)


