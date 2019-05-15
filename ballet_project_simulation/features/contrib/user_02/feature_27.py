from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Bsmt Cond", "BsmtQual", "BsmtExposure",
         "BsmtFinType1", "BsmtFinType2"]


def impute_mode(df):
    result = df['Bsmt Cond'].copy()
    mask = (df['Bsmt Cond'].isnull()
            & df.drop('Bsmt Cond', axis=1).notnull().any(axis=1))
    mask_not_null = result.notnull()
    result.[mask] = result[mask_not_null].mode()
    return result


transformer = [
    ballet.eng.SimpleFunctionTransformer(impute_mode),
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Imputed basement condition"
feature = Feature(input=input, transformer=transformer, name=name)
