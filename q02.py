##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
### Punto 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
TD_= pd.read_csv("tbl0.tsv", sep="\t")
TD_2=tb.groupby('_c1')['_c2'].mean()
print(TD_2)
