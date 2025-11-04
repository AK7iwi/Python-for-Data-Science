import numpy as np
from PIL import Image
import time

# Test with a small image (create test image)
test_image = Image.new('RGB', (100, 100), color='red')

# Method 1: Your current approach (np.asarray)
start_time = time.time()
for _ in range(1000):
    result1 = np.asarray(test_image)
time1 = time.time() - start_time

# Method 2: Alternative with np.array
start_time = time.time()
for _ in range(1000):
    result2 = np.array(test_image)
time2 = time.time() - start_time

print(f'np.asarray() time: {time1:.4f}s')
print(f'np.array() time: {time2:.4f}s')
print(f'Performance difference: {((time2-time1)/time1)*100:.1f}%')
print(f'Result shapes match: {result1.shape == result2.shape}')
print(f'Result dtypes match: {result1.dtype == result2.dtype}')
