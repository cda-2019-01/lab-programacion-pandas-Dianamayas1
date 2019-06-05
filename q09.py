##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
### Punto 9
import pandas as pd
import numpy as np
TD_= pd.read_csv("tbl0.tsv", sep="\t")
dfaux = TD_.groupby('_c1')['_c2'].apply(list)
TD_9 = pd.DataFrame()
TD_9['_c1'] = dfaux.keys()
TD_9['lista'] = [elemt for elemt in dfaux]
TD_9['lista'] = [":".join(str(v) for v in sorted(elemt)) for elemt in TD_9['lista']]
print(TD_9)

