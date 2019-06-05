##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
### Punto 8
import pandas as pd
import numpy as np
TD_= pd.read_csv("tbl0.tsv", sep="\t")
TD_8=TD_.copy()
TD_8['anio'] = TD_8['_c3'].str.split('-').str[0]
print(TD_8)
