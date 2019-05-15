from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Mas Vnr Area"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Mas Vnr Area".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Mas Vnr Area unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
