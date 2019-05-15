from ballet import Feature
from sklearn.impute import SimpleImputer

# BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF, BsmtFullBath and BsmtHalfBath :
# missing values are likely zero for having no basement

input = ["Bsmt Full Bath"]
transformer = SimpleImputer(strategy="mean")
name = "Imputed basement full bathrooms"
feature = Feature(input=input, transformer=transformer, name=name)
