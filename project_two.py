"""
Class:   CS-510
Author:  Malgorzata Debska
Date:    January 2026

Description:
This program simulates operating system performance monitoring and optimization
by displaying disk usage, CPU statistics, memory management details, threading 
lifecycles, and error handling using Python and psutil.
"""

import os
import psutil
import sys
import threading
import time

def printBlankLines(lines: int):
    """Utility to print blank lines for formatted output."""
    for _ in range(lines):
        print("")

def threadTaskOne(num):
    """Function for Thread 1 to calculate a cube and display its unique ID."""
    # Requirement 4A: Display execution state and Thread ID
    thread_id = threading.get_ident()
    print(f"[EXECUTION] Thread 1 (ID: {thread_id}) is calculating {num}^3...")
    time.sleep(1)  # Simulate workload
    print(f"Thread 1 Result: {num ** 3}")

def threadTaskTwo(num):
    """Function for Thread 2 to calculate a square and display its unique ID."""
    # Requirement 4A: Display execution state and Thread ID
    thread_id = threading.get_ident()
    print(f"[EXECUTION] Thread 2 (ID: {thread_id}) is calculating {num}^2...")
    time.sleep(1)  # Simulate workload
    print(f"Thread 2 Result: {num ** 2}")

def getFileDiskUsageStatistics() -> None:
    """Queries disk usage and reads file attributes for formatted output."""
    print("--- Disk Resource Usage ---")
    
    # Requirement 1Ai: Total and free disk space
    disk = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space:  {disk.free / (1024 ** 3):.2f} GB")

    # Requirement 1Aii: Read file attributes and size
    file_name = "projecttwo.txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write("GlobalFinTech Inc. sample data for optimization testing.")

    file_stats = os.stat(file_name)
    print(f"File Name:      {file_name}")
    print(f"File Size:      {file_stats.st_size} bytes")
    print(f"Last Modified:  {file_stats.st_mtime}")
    printBlankLines(1)

def getCpuStatistics() -> None:
    """Reads and formats CPU size and usage statistics."""
    print("--- CPU Resource Statistics ---")
    # Requirement 2A: CPU size (cores) and usage
    print(f"CPU Cores (Logical): {psutil.cpu_count(logical=True)}")
    print(f"Current CPU Usage:   {psutil.cpu_percent(interval=1)}%")
    printBlankLines(1)

def getMemoryStatistics() -> None:
    """Reads and formats total, used, and virtual memory usage."""
    print("--- Memory Resource Usage ---")
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    # Requirement 3A: Total, Used, and Virtual (Swap) Memory
    print(f"Total Physical Memory: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Used Physical Memory:  {mem.used / (1024 ** 3):.2f} GB")
    print(f"Virtual Memory (Swap): {swap.total / (1024 ** 3):.2f} GB")
    print(f"Memory Usage Percent:  {mem.percent}%")
    printBlankLines(1)

def showThreadingExample() -> None:
    """Demonstrates thread creation, execution, and destruction lifecycle."""
    print("--- Concurrency and Threading ---")
    
    # Requirement 4A: Creation output
    print("[CREATION] Initializing two separate threads...")
    t1 = threading.Thread(target=threadTaskOne, args=(5,))
    t2 = threading.Thread(target=threadTaskTwo, args=(10,))

    # Start threads
    t1.start()
    t2.start()

    # Requirement 4A: Wait for threads to finish (Destroyed state)
    t1.join()
    t2.join()
    print("[DESTROYED] All threads have finished and resources are released.")
    printBlankLines(1)

def showErrorHandling() -> None:
    """Demonstrates error handling for system exceptions (divide by zero)."""
    print("--- Error/Fault Handling ---")
    # Requirement 5A: Cause an error, catch it, and state it clearly
    try:
        print("Attempting to divide 100 by 0...")
        result = 100 / 0
    except ZeroDivisionError as e:
        print(f"CAUGHT ERROR: {e} (Division by zero is not allowed).")
    finally:
        print("System remains stable; error was handled successfully.")
    printBlankLines(1)

def main() -> int:
    """Main execution entry point for the OS simulator."""
    print("GlobalFinTech OS Optimization Simulator Starting")
    print("================================================")

    getFileDiskUsageStatistics()
    getCpuStatistics()
    getMemoryStatistics()
    showThreadingExample()
    showErrorHandling()

    print("Simulator execution complete.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
