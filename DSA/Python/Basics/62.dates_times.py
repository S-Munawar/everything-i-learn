# Dates and Times
# - datetime: Built-in module for manipulating dates and times.
# - datetime.date: Represents a date (year, month, and day).
# - datetime.time: Represents a time (hour, minute, second, microsecond).
# - datetime.datetime: Represents both a date and a time.
# - strftime(): Method used to format datetime objects into readable strings.

import datetime
import time

print("--- 📅 Dates and Times in Python 📅 ---")

# --- 1. Getting the Current Date and Time ---
print("\n--- 1. Getting Current Date and Time ---")
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime}")

current_date = datetime.date.today()
print(f"Current Date: {current_date}")

# --- 2. Creating Custom Date and Time Objects ---
print("\n--- 2. Creating Custom Date and Time Objects ---")
# Creating a date (Year, Month, Day)
my_birthday = datetime.date(2004, 12, 31)
print(f"My Birthday: {my_birthday}")

# Creating a time (Hour, Minute, Second)
my_alarm = datetime.time(7, 30, 0)
print(f"My Alarm: {my_alarm}")

# Creating a datetime (Year, Month, Day, Hour, Minute, Second)
new_year = datetime.datetime(2027, 1, 1, 0, 0, 0)
print(f"New Year 2025: {new_year}")

# --- 3. Formatting Dates (strftime) ---
print("\n--- 3. Formatting Dates (strftime) ---")
# strftime allows you to format a datetime object into a string
# Common formatting codes:
# %Y: Year with century (e.g., 2023)
# %m: Month as a zero-padded decimal number (01-12)
# %d: Day of the month as a zero-padded decimal number (01-31)
# %H: Hour (24-hour clock)
# %M: Minute
# %S: Second
# %B: Month's full name

formatted_date = current_datetime.strftime("%B %d, %Y - %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# --- 4. Measuring Time (time module) ---
print("\n--- 4. Measuring Time (time module) ---")
# The time module is useful for tracking how long a piece of code takes to run
print("Sleeping for 1 second...")
start_time = time.time() # Records the current time in seconds since the Epoch
time.sleep(1) # Pauses execution for 1 second
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Woke up! Elapsed time: {elapsed_time:.2f} seconds")

# --- ⏱️ Time Complexities (Average Case) ---
# datetime.datetime.now() - O(1) Time - Constant time to fetch system clock.
# time.time()             - O(1) Time - Constant time to fetch system clock.
# strftime()              - O(1) Time - Constant time relative to fixed string length.
