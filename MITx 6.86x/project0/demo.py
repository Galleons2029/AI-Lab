import numpy as np

x = np.random.random([10, 1])
PYTHONBREAKPOINT = 0


filename = __file__
import pdb; pdb.set_trace()
print(f'path = {filename}')

print(x)

