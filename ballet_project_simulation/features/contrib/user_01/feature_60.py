from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Low Qual Fin SF"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Low Qual Fin SF".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Low Qual Fin SF unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
