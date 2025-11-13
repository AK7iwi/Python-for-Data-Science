from callLimit import callLimit

# Test 1a - Valid input: Basic input
print("Test 1a - Valid input: Basic input\n")

@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()

print("\n--------------------------------\n")

# Test b - Valid input: Basic input
print("Test 1b - Valid input: Basic input\n")

@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(4):
    f()
    g()

print("\n--------------------------------\n")
