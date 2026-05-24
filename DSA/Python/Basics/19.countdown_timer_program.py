import time

# Countdown Timer Program
# - An interactive program that counts down from a user-specified time.
# - Combines for-loops with a negative step, the time.sleep() function, 
#   and math to calculate hours, minutes, and seconds.

print("--- ⏱️ Countdown Timer ⏱️ ---")

# 1. Ask the user for the number of seconds to count down from
my_time = int(input("Enter the total time in seconds: "))

# 2. Iterate backwards from my_time down to 1
# range(start, stop, step) -> stop is 0 because it is exclusive!
for x in range(my_time, 0, -1):
    
    # 3. Calculate Hours, Minutes, and Seconds
    # 'x' is the total number of seconds remaining
    seconds = x % 60
    minutes = (x // 60) % 60  # // is integer division (throws away the decimal)
    hours = x // 3600

    # 4. Format the time using f-strings and zero-padding (from lesson 15!)
    # :02 means pad the number with zeros until it is 2 characters long
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    # 5. Pause the program execution for 1 exact second
    time.sleep(1)

print("TIME'S UP! ⏰")
