##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
### Punto 1
import pandas as pd
import numpy as np
TD_= pd.read_csv("tbl0.tsv", sep="\t")
TD_1=TD_.groupby('_c1').count()['_c2']
print(TD_1)
