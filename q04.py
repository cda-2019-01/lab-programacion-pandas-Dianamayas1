##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
### Punto 4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
TD_= pd.read_csv("tbl1.tsv", sep="\t")
TD_4=TD_['_c4'].unique()
TD_4= [line.upper() for line in TD_4]
TD_4.sort()
print(TD_4)

