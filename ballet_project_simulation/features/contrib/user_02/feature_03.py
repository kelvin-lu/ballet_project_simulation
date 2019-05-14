from ballet import Feature
import ballet.eng
import pandas as pd


def fill_garage(df):
    return df["Year Built"].where(pd.notnull, df["Garage Yr Blt"])


input = ["Garage Yr Blt", "Year Built"]
transformer = ballet.eng.SimpleFunctionTransformer(fill_garage)
name = "Impute garage year built"
feature = Feature(input=input, transformer=transformer, name=name)
