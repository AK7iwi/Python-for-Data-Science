from new_student import Student

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

student = Student(name="Edward", surname="agle")
print(student)

print("\n--------------------------------\n")

# Test 2 - Invalid input: Basic input
print("Test 2 - Invalid input: Basic input\n")

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except (TypeError) as e:
    print(f"TypeError: {e}")

print("\n--------------------------------\n")
