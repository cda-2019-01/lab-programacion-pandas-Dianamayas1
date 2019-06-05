##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
### Punto 7
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
TD_7= pd.read_csv("tbl0.tsv", sep="\t")
tbl=TD_.copy()
tbl['suma'] = tbl['_c0'] + tbl['_c2']
print(tbl)
