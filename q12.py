##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
### Punto 12
import pandas as pd
import numpy as np
TD_= pd.read_csv('tbl2.tsv', sep='\t')
TD_12=TD_.groupby('_c5a')['_c5b'].sum()
print(TD_12)

