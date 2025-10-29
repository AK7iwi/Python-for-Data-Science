import numpy as np

arr = np.array([1, 2, 3])
print("arr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[1, 2, 3]])
print("\narr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[1], [2], [3]])
print("\narr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\narr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\narr =", arr)
print("arr.shape =", arr.shape)
print("arr.truncated shape =", arr.shape[:2])


try:
    array = np.array([[1, "Invalid", 3], [4, 5]])
    print(array)
except ValueError as e:
    print(f"ValueError: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
except Exception as e:
    print(f"Exception: {e}")
