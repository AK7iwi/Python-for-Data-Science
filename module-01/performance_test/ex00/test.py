import numpy as np
import time

# Test data
height = [2.71, 1.15, 1.80, 1.65, 1.70]
weight = [165.3, 38.4, 75.0, 60.0, 70.0]
limit = 26

# Method 1: Your current approach (np.asarray)
start = time.time()
for _ in range(10000):
    bmi = np.asarray(weight) / (np.asarray(height) ** 2)
    result = (np.asarray(bmi) > limit).tolist()
time1 = time.time() - start

# Method 2: Alternative with np.array
start = time.time()
for _ in range(10000):
    bmi = np.array(weight) / (np.array(height) ** 2)
    result = (np.array(bmi) > limit).tolist()
time2 = time.time() - start

print(f'np.asarray() time: {time1:.4f}s')
print(f'np.array() time: {time2:.4f}s')
print(f'Performance difference: {((time2-time1)/time1)*100:.1f}%')