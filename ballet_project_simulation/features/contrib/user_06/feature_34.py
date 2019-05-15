from ballet import Feature
import ballet.eng


def is_remod(df):
    return df["Year Built"] != df["Year Remod/Add"]


input = ["Year Built", "Year Remod/Add"]
transformer = ballet.eng.SimpleFunctionTransformer(is_remod)
name = "Is remodeled"
feature = Feature(input=input, transformer=transformer, name=name)
