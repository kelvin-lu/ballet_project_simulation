from ballet import Feature
from ballet.eng import SimpleFunctionTransformer


def calc_qual(df):
    return df["Overall Qual"] - df["Overall Cond"]


input = ["Overall Qual", "Overall Cond"]
transformer = SimpleFunctionTransformer(calc_qual)
name = "Qual"
feature = Feature(input=input, transformer=transformer, name=name)
