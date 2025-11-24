"""
Author: Malgorzata Debska
Course: CS-510
Date: 11-24-2025
Assignment: Multi-threading Activity
Description:
This program demonstrates basic multi-threading in Python
using the threading module. Two separate threads call two
different functions and run concurrently.
"""

import threading
import time

def task_one():
    """Function executed by the first thread."""
    for i in range(5):
        print("task_one() ? iteration", i+1)
        time.sleep(0.5)

def task_two():
    """Function executed by the second thread."""
    for i in range(5):
        print("task_two() ? iteration", i+1)
        time.sleep(0.5)

def main():
    # Create threads and assign target functions
    thread1 = threading.Thread(target=task_one, name="Thread-1")
    thread2 = threading.Thread(target=task_two, name="Thread-2")

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()

    print("Both threads have completed execution.")

if __name__ == "__main__":
    main()
