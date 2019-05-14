from ballet import Feature
from ballet.eng import NullFiller, SimpleFunctionTransformer


def calc_age(df):
    return df["Yr Sold"] - df["Year Remod/Add"]


input = ["Yr Sold", "Year Remod/Add"]
transformer = [SimpleFunctionTransformer(calc_age), NullFiller()]
name = "Years since remodeled"
feature = Feature(input=input, transformer=transformer, name=name)
