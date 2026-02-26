#%%
import pandas as pd

def transformation(df):
    ftr = (df["User_Rating"] > 4.6) & (df["API_Available"] == "Yes")

    df_transformed = df[ftr]

    return df_transformed