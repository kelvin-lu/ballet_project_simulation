from ballet import Feature
import ballet.eng


input = ["Full Bath", "Half Bath", "Bsmt Full Bath", "Bsmt Half Bath"]


def calc_bath(df):
    return (
        df["Full Bath"]
        + 0.5 * df["Half Bath"]
        + df["Bsmt Full Bath"]
        + 0.5 * df["Bsmt Half Bath"]
    )


transformer = ballet.eng.SimpleFunctionTransformer(func=calc_bath)
name = "Total number of bathrooms"
feature = Feature(input=input, transformer=transformer, name=name)
