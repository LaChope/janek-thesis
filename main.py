import pandas as pd
import handle_pressure

if __name__ == '__main__':
    df = handle_pressure.get_pressure_dataframe("data/2021/7-červenec 21/BARO/PRESSURE_1_01.xlsx")
    df.to_excel("./Test.xlsx")
