"""
Class:   CS-510
Author:  Malgorzata Debska
Date:    January 2026

Description:
This program simulates operating system performance monitoring and optimization
by displaying disk usage, CPU statistics, memory management details, threading,
and error handling using Python and psutil.
"""

import os
import psutil
import sys
import threading

def printBlankLines(lines: int):
    for _ in range(lines):
        print("")

def printMsg1(num):
    print("Thread 1 cubed:", num ** 3)

def printMsg2(num):
    print("Thread 2 squared:", num ** 2)

"""
Displays disk usage statistics and file information.
"""
def getFileDiskUsageStatistics() -> None:
    print("Getting Disk Statistics")

    # Disk usage
    disk = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

    # File statistics
    file_name = "projecttwo.txt"

    # Create file if it does not exist
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write("Sample data for disk usage testing.")

    file_stats = os.stat(file_name)
    print(f"File Name: {file_name}")
    print(f"File Size: {file_stats.st_size} bytes")
    print(f"Last Modified: {file_stats.st_mtime}")

    printBlankLines(2)

"""
Displays system memory and virtual memory statistics.
"""
def getMemoryStatistics() -> None:
    print("Getting Memory Statistics")

    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {mem.used / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Memory Usage Percentage: {mem.percent}%")

    printBlankLines(2)

"""
Displays CPU statistics including usage and core count.
"""
def getCpuStatistics() -> None:
    print("Getting CPU Statistics")

    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

    printBlankLines(2)

"""
Demonstrates concurrency using threading.
"""
def showThreadingExample() -> None:
    print("Demonstrating Threading")

    thread1 = threading.Thread(target=printMsg1, args=(3,))
    thread2 = threading.Thread(target=printMsg2, args=(4,))

    print("Starting Threads")
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Threads Completed")
    printBlankLines(2)

"""
Demonstrates error handling using a divide-by-zero exception.
"""
def showErrorHandling() -> None:
    print("Demonstrating Error Handling")

    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
    except MemoryError:
        print("Memory Error!")
    else:
        print("Result:", result)
    finally:
        print("Execution complete.")

    printBlankLines(2)

def main() -> int:
    print("Starting Program")
    print("=============================")

    getFileDiskUsageStatistics()
    getCpuStatistics()
    getMemoryStatistics()
    showThreadingExample()
    showErrorHandling()

    return 0

if __name__ == '__main__':
    sys.exit(main())
