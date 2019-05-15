from ballet import Feature
import ballet.eng


input = ["Year Built", "Year Remod/Add"]


def is_remod(df):
    return df["Year Built"] != df["Year Remod/Add"]


transformer = ballet.eng.SimpleFunctionTransformer(is_remod)
name = "Is remodeled"
feature = Feature(input=input, transformer=transformer, name=name)
