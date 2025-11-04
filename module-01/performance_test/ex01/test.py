import numpy as np
import time

# Test data
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
start, end = 0, 2

# Method 1: Your current approach (np.asarray)
start_time = time.time()
for _ in range(10000):
    family_array = np.asarray(family)
    sliced_array = family_array[start:end]
    result = sliced_array.tolist()
time1 = time.time() - start_time

# Method 2: Alternative with np.array
start_time = time.time()
for _ in range(10000):
    family_array = np.array(family)
    sliced_array = family_array[start:end]
    result = sliced_array.tolist()
time2 = time.time() - start_time

print(f'np.asarray() time: {time1:.4f}s')
print(f'np.array() time: {time2:.4f}s')
print(f'Performance difference: {((time2-time1)/time1)*100:.1f}%')
