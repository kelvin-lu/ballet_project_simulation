from ballet import Feature
import ballet.eng


def order_pool_quality(df):
    return df["Pool QC"].map({"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})


def impute_by_pool_area_and_overall_qual(df):
    result = df["Pool QC"].copy()
    mask = (df["Pool QC"] == 0) & (df["Pool Area"] > 0)
    result.loc[mask] = (df.loc[mask, "Overall Qual"] + 1) // 2
    return result


input = ["Pool QC", "Pool Area", "Overall Qual"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    ballet.eng.SimpleFunctionTransformer(order_pool_quality),
    ballet.eng.SimpleFunctionTransformer(impute_by_pool_area_and_overall_qual),
]
name = "Imputed pool quality"
feature = Feature(input=input, transformer=transformer, name=name)
