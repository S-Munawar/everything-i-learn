# Alarm Clock Program
# - An interactive practice script demonstrating the use of 'time' and 'datetime' modules.
# - Takes a user input for an alarm time and waits until the system clock matches it.
# - Uses carriage return (\r) to create a dynamically updating clock in the terminal.

import time
import datetime

print("--- ⏰ Python Alarm Clock ⏰ ---")

def set_alarm():
    print("Set your alarm time in 24-hour format (HH:MM:SS)")
    print("Example: 14:30:00 for 2:30 PM")
    
    alarm_time = input("Enter alarm time: ").strip()
    
    # Basic validation check for string length
    if len(alarm_time) != 8 or alarm_time.count(":") != 2:
        print("❌ Invalid format! Please use HH:MM:SS.")
        return

    print(f"\nAlarm successfully set for {alarm_time}...")
    print("Waiting...\n")
    
    is_running = True
    
    while is_running:
        # Get the current time as a formatted string
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Print the current time on the same line using \r (carriage return)
        print(f"Current time: {current_time}", end="\r") 
        
        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("\n") # Move to a new line before printing the wake up message
            print("🚨 WAKE UP! 🚨 WAKE UP! 🚨 WAKE UP! 🚨")
            
            # \a is the ASCII bell character, which might play a sound in some terminals
            print("\a\a\a", end="")
            
            is_running = False
            
        # Pause the loop for 1 second to prevent high CPU usage
        time.sleep(1)

if __name__ == "__main__":
    # try-except block to gracefully handle user pressing Ctrl+C
    try:
        set_alarm()
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled by user. Goodbye!")

# --- ⏱️ Time Complexities (Average Case) ---
# time.sleep(1)           - O(1) Time - Constant time pause per iteration.
# datetime formatting     - O(1) Time - Constant time to format a short string.
# Overall Execution Time  - O(N) Time - Where N is the number of seconds until the alarm triggers.
