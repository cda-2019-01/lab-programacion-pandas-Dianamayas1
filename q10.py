##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
## Punto 10
import pandas as pd
import numpy as np
TD_ = pd.read_csv("tbl1.tsv", sep="\t")
dfaux = TD_.groupby('_c0')['_c4'].apply(list)
TD_10 = pd.DataFrame()
TD_10 ['_c0'] = dfaux.keys()
TD_10 ['lista'] = [elemt for elemt in dfaux]
TD_10 ['lista'] = [",".join(str(v) for v in sorted(elemt)) for elemt in TD_10['lista']]
print(TD_10)
