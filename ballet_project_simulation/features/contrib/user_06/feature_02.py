import pandas as pd
from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = ["Year Built", "Garage Yr Blt"]


def calc_age(df):
    return df["Year Built"].where(pd.notnull, df["Garage Yr Blt"])


transformer = SimpleFunctionTransformer(calc_age)
name = "Year built fill"
feature = Feature(input=input, transformer=transformer, name=name)
