import pandas as pd

# List all pandas exceptions
print("=== PANDAS EXCEPTIONS ===")
exceptions = [e for e in dir(pd.errors) if not e.startswith("__")]
for exc in sorted(exceptions):
    print(f"pd.errors.{exc}")