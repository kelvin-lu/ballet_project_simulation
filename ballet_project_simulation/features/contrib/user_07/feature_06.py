from ballet import Feature
import sklearn.impute

# BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF, BsmtFullBath and BsmtHalfBath :
# missing values are likely zero for having no basement
input = ["Bsmt Half Bath"]
transformer = sklearn.impute.SimpleImputer(strategy="mean")
name = "Imputed basement half bathrooms"
feature = Feature(input=input, transformer=transformer, name=name)
