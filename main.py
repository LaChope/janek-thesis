import pandas as pd
import LKPR_pressure
import glob
import matplotlib.pyplot as plt


baro_data = glob.glob("./data/2021/*/BARO/PRESSURE_1_*.xlsx")

if __name__ == '__main__':
    df_list = []
    # for i in range(len(baro_data)):
    for i in range(2):
        df = LKPR_pressure.get_pressure_dataframe(str(baro_data[i]))
        df_list.append(df)
    concat_df = pd.concat(df_list)
    plt.scatter(concat_df["CREATEDATE"], concat_df["PA_QNH (HPA)"])
    plt.xlabel("Date")
    plt.ylabel("Pressure (HPA)")
    plt.show()
    concat_df.to_excel("./PRESSURE.xlsx")
