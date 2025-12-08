# Author: Malgorzata Debska
# Date: December 8, 2025
# Description: CS 510
# This program demonstrates process synchronization using a semaphore
# to prevent deadlocks and control concurrent access to a shared resource.

import threading
import time
import random

# Initialize semaphore with a limit of 2 concurrent threads
# You can change the value to see how it affects synchronization.
semaphore_limit = 2
semaphore = threading.Semaphore(semaphore_limit)

def worker(thread_id):
    """
    Simulates a process accessing a shared resource.
    The semaphore ensures that only a limited number of threads
    may enter the critical section at once.
    """
    print(f"Thread {thread_id} is waiting to acquire the semaphore...")

    # Acquire semaphore (enter critical section)
    semaphore.acquire()
    print(f"Thread {thread_id} has entered the critical section.")

    # Simulate work inside the critical section
    time.sleep(random.uniform(0.5, 2.0))

    print(f"Thread {thread_id} is leaving the critical section.")

    # Release semaphore (exit critical section)
    semaphore.release()

def main():
    print(f"Initializing semaphore with a limit of {semaphore_limit}.\n")
    threads = []

    # Create and start 5 worker threads
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("\nAll threads have completed execution.")

if __name__ == "__main__":
    main()
