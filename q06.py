##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
### Punto 6
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
TD_= pd.read_csv("tbl0.tsv", sep="\t")
TD_6=tb.groupby('_c1').sum()['_c2']
print(TD_6)
