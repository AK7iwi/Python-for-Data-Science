import time
from datetime import datetime

# Get current time in seconds since epoch
current_time = time.time()

# Format the seconds with comma separators and scientific notation
formatted_seconds = f"{current_time:,.4f}"
scientific_notation = f"{current_time:.2e}"

# Get current date and format it
current_date = datetime.now()
formatted_date = current_date.strftime("%b %d %Y")

# Print the results
print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(formatted_date)
