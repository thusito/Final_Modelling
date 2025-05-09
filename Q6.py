import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4, 4),
                  index=[1, 2, 3, 4],
                  columns=['a', 'b', 'c', 'd'])

# access the same scalar three ways

# 1) “index” style (column first, then row label)
val_index = df['b'][3]        # or equivalently df.b[3]

# 2) .loc  — label-based (row label, column label)
val_loc   = df.loc[3, 'b']

# 3) .iloc — purely position-based (row-pos 2, col-pos 1)
val_iloc  = df.iloc[2, 1]

print(val_index, val_loc, val_iloc, sep='\n')

#Because they reference the identical cell, the printed values will be identical
