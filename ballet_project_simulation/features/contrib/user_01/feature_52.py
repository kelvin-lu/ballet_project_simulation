from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Year Remod/Add"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Year Remod/Add".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Year Remod/Add unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
