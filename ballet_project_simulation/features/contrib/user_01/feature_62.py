from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Bsmt Full Bath"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Bsmt Full Bath".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Bsmt Full Bath unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
