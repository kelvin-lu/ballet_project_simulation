from ballet import Feature
import ballet.eng


def calc_age(df):
    return df["Yr Sold"] - df["Year Remod/Add"]


input = ["Yr Sold", "Year Remod/Add"]
transformer = ballet.eng.SimpleFunctionTransformer(calc_age)
name = "Years since remodeled"
feature = Feature(input=input, transformer=transformer, name=name)
