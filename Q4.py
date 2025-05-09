import numpy as np

a = np.arange(0, 12)

# all operations are done in-place on the same array ‘a’ 
a *= (2 * a + 1)  # maps n  →  n (2n+1)  = 2 n² + n
a.shape = (6, 2)  # turn the 12 numbers into the 6 × 2 table

print(a)
