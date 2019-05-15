from ballet import Feature
import ballet.eng


def impute(df):
    # Impute mode veneer type for houses with no type but positive veneer area
    result = df["Mas Vnr Type"].copy()
    mask = (df["Mas Vnr Type"] == "None") & (df["Mas Vnr Area"] > 0)
    mask_not_none = df["Mas Vnr Type"] != "None"
    result.loc[mask] = df.loc[mask_not_none, "Mas Vnr Type"].mode()
    return result


order = {"None": 0, "BrkCmn": 0, "BrkFace": 1, "Stone": 2}

input = ["Mas Vnr Type", "Mas Vnr Area"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    ballet.eng.SimpleFunctionTransformer(impute),
    ballet.eng.SimpleFunctionTransformer(lambda ser: ser.map(order)),
]
name = "Imputed masonry veneer type"
feature = Feature(input=input, transformer=transformer, name=name)
