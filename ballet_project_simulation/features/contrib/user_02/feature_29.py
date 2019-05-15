from ballet import Feature
import ballet.eng


input = ["Yr Sold", "Year Remod/Add"]


def calc_age(df):
    return df["Yr Sold"] - df["Year Remod/Add"]


transformer = ballet.eng.SimpleFunctionTransformer(func=calc_age)
name = "Age"
age = Feature(input=input, transformer=transformer, name="Age")
