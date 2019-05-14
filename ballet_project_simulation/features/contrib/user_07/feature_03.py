from ballet import Feature
from sklearn.impute import SimpleImputer

# BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF, BsmtFullBath and BsmtHalfBath :
# missing values are likely zero for having no basement

input = ["Bsmt Unf SF"]
transformer = SimpleImputer(strategy="mean")
name = "Imputed unfinished square feet of basement area"
feature = Feature(input=input, transformer=transformer, name=name)
