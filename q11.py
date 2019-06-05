##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
### Punto 11
import pandas as pd
import numpy as np
TD_= pd.read_csv("tbl2.tsv", sep="\t")
TD_['_c5'] = TD_['_c5a'] + ":" + TD_['_c5b'].astype('str')
dfaux = TD_.groupby('_c0')['_c5'].apply(list)
TD_11 = pd.DataFrame()
TD_11['_c0'] = dfaux.keys()
TD_11['lista'] = [elemt for elemt in dfaux]
TD_11['lista'] = [",".join(str(v) for v in sorted(elemt)) for elemt in TD_11['lista']]
print(TD_11)
