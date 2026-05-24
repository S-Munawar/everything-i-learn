# Multithreading
# - thread: A flow of execution. Like a separate order of instructions.
# - multithreading: Used to perform multiple tasks concurrently (simultaneously).
# - Global Interpreter Lock (GIL): A mutex in CPython that prevents multiple threads from executing Python bytecodes at once. This means multithreading is concurrent, but not truly parallel in Python.
# - I/O bound tasks: Tasks that spend most of their time waiting (network requests, reading/writing files, API calls). Multithreading is EXCELLENT for this.
# - CPU bound tasks: Tasks that require heavy processing (complex math, image rendering). Multithreading does NOT speed this up in Python due to the GIL (use multiprocessing instead).

import threading
import time

print("--- 🧵 Multithreading in Python 🧵 ---")

# Let's define three I/O bound tasks (simulated using time.sleep)
def walk_dog():
    print("🐕 You started walking the dog...")
    time.sleep(3) 
    print("🐕 You finished walking the dog!")

def take_out_trash():
    print("🗑️ You started taking out the trash...")
    time.sleep(2)
    print("🗑️ You finished taking out the trash!")

def get_mail():
    print("📬 You started getting the mail...")
    time.sleep(1)
    print("📬 You finished getting the mail!")

# --- 1. Synchronous Execution (Sequential) ---
print("\n--- 1. Synchronous Execution (One by one) ---")
start_time_sync = time.time()

walk_dog()
take_out_trash()
get_mail()

end_time_sync = time.time()
print(f"⏱️ Synchronous Total Time: {end_time_sync - start_time_sync:.2f} seconds")
# Total time should be roughly 3 + 2 + 1 = 6 seconds.


# --- 2. Multithreading Execution (Concurrent) ---
print("\n--- 2. Multithreading Execution (Concurrent) ---")
start_time_thread = time.time()

# Creating threads
# target: the function you want the thread to execute (pass reference, no parentheses!)
thread1 = threading.Thread(target=walk_dog)
thread2 = threading.Thread(target=take_out_trash)
thread3 = threading.Thread(target=get_mail)

# Starting the threads (They begin executing their target functions)
thread1.start()
thread2.start()
thread3.start()

# .join() makes the main program (MainThread) wait for these threads to finish
# If we don't use .join(), the main program will keep executing and print the total time prematurely!
thread1.join()
thread2.join()
thread3.join()

end_time_thread = time.time()
print(f"⏱️ Multithreading Total Time: {end_time_thread - start_time_thread:.2f} seconds")
# Total time should be roughly equal to the longest task (3 seconds).


# --- 3. Thread Information ---
print("\n--- 3. Active Threads Info ---")
# The main program itself runs on a thread (MainThread)
print(f"Total active threads at this moment: {threading.active_count()}")
print(f"Current thread executing this line: {threading.current_thread().name}")

print("List of active threads:")
for thread in threading.enumerate():
    print(f" - {thread.name}")


# --- ⏱️ Time Complexities (Overheads) ---
# threading.Thread() - O(1) Time - Constant time to initialize a thread object.
# thread.start()     - O(1) Time - Constant time to spawn the OS thread.
# Note: For I/O bound tasks, N tasks taking max T time will complete in roughly O(T) time instead of O(N*T).
