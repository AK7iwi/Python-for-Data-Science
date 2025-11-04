import numpy as np
import time

# Test data (simulate image array)
array = np.random.randint(0, 255, (1000, 1000, 3), dtype=np.uint8)

# Method 1: Your current approach (array.copy())
start_time = time.time()
for _ in range(100):
    red_filtered = array.copy()
    red_filtered[:, :, 1] = 0
    red_filtered[:, :, 2] = 0
time1 = time.time() - start_time

# Method 2: Alternative with np.array()
start_time = time.time()
for _ in range(100):
    red_filtered = np.array(array)
    red_filtered[:, :, 1] = 0
    red_filtered[:, :, 2] = 0
time2 = time.time() - start_time

# Method 3: Alternative with np.asarray()
start_time = time.time()
for _ in range(100):
    red_filtered = np.asarray(array)
    red_filtered[:, :, 1] = 0
    red_filtered[:, :, 2] = 0
time3 = time.time() - start_time

print(f'array.copy() time: {time1:.4f}s')
print(f'np.array() time: {time2:.4f}s')
print(f'np.asarray() time: {time3:.4f}s')
print(f'array.copy() vs np.array(): {((time2-time1)/time1)*100:.1f}% difference')
print(f'array.copy() vs np.asarray(): {((time3-time1)/time1)*100:.1f}% difference')

print('\n=== Memory Safety Test ===')

# Test memory safety
test_array = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 255]]])
print(f'Original array: {test_array}')

# Method 1: array.copy() - SAFE
safe_copy = test_array.copy()
safe_copy[:, :, 1] = 0
print(f'After array.copy() modification: {safe_copy}')
print(f'Original array unchanged: {test_array}')

# Method 2: np.asarray() - POTENTIALLY UNSAFE
unsafe_copy = np.asarray(test_array)
unsafe_copy[:, :, 1] = 0
print(f'After np.asarray() modification: {unsafe_copy}')
print(f'Original array affected: {test_array}')
print(f'Are they the same object? {unsafe_copy is test_array}')
