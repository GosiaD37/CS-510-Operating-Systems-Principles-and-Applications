"""
    Class:   CS-510
    Author:  Malgorzata Debska
    Date:    January 14, 2026

    Description: This application monitors system resources (Disk, CPU, Memory), 
                 demonstrates multi-threaded concurrency with lifecycle tracking, 
                 and implements error handling for system stability.
"""  
import os
import psutil
import sys
import threading
import time

def printBlankLines(lines: int):
    for i in range(lines):
        print("")

def printMsg1(num):
    # Requirement 4.A: Display thread ID and execution status
    thread_id = threading.get_ident()
    print(f"[EXECUTE] Thread 1 (ID: {thread_id}) is calculating {num}^3...")
    time.sleep(1) # Simulating work
    print(f"Thread 1 Result (cubed): {num * num * num}")

def printMsg2(num):
    # Requirement 4.A: Display thread ID and execution status
    thread_id = threading.get_ident()
    print(f"[EXECUTE] Thread 2 (ID: {thread_id}) is calculating {num}^2...")
    time.sleep(1) # Simulating work
    print(f"Thread 2 Result (squared): {num * num}")

def getFileDiskUsageStatistics() -> None:
    """Requirement 1: Query and display total/free disk space and file attributes."""
    print("--- Disk Resource Usage ---")
    
    # Part 1: Total and Free disk space
    disk_info = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk_info.total / (1024**3):.2f} GB")
    print(f"Free Disk Space:  {disk_info.free / (1024**3):.2f} GB")
    
    # Part 2: File attributes and size
    file_name = "./projecttwo.txt"
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write("This is a sample text file for disk resource testing.")
    
    file_stats = os.stat(file_name)
    print(f"File Name: {file_name}")
    print(f"File Size: {file_stats.st_size} bytes")
    print(f"Last Accessed: {time.ctime(file_stats.st_atime)}")

    printBlankLines(1)

def getMemoryStatistics() -> None:
    """Requirement 3: Read total memory, used memory, and virtual memory usage."""
    print("--- Memory Resource Usage ---")
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    print(f"Total Physical Memory: {mem.total / (1024**3):.2f} GB")
    print(f"Used Physical Memory:  {mem.used / (1024**3):.2f} GB ({mem.percent}%)")
    print(f"Virtual (Swap) Memory Used: {swap.used / (1024**3):.2f} GB")

    printBlankLines(1)

def getCpuStatistics() -> None:
    """Requirement 2: Read CPU size (cores) and usage statistics."""
    print("--- CPU Resource Statistics ---")
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count_logical = psutil.cpu_count()
    cpu_count_phys = psutil.cpu_count(logical=False)
    
    print(f"CPU Usage (Last 1s): {cpu_usage}%")
    print(f"Logical CPU Cores:   {cpu_count_logical}")
    print(f"Physical CPU Cores:  {cpu_count_phys}")

    printBlankLines(1)

def showThreadingExample() -> None:
    """Requirement 4: Create threads, show IDs, and track creation/execution/destruction."""
    print("--- Concurrency and Threading ---")
   
    # Create threads
    t1 = threading.Thread(target=printMsg1, args=(5,))
    t2 = threading.Thread(target=printMsg2, args=(10,))
    
    print(f"[CREATE] Thread 1 created.")
    print(f"[CREATE] Thread 2 created.")

    # Start execution
    t1.start()
    t2.start()
    
    # Wait for completion (destruction phase)
    t1.join()
    t2.join()
    
    print("[DESTROY] Thread 1 has finished and resources are released.")
    print("[DESTROY] Thread 2 has finished and resources are released.")

    printBlankLines(1)

def showErrorHandling() -> None:
    """Requirement 5: Implement a function that causes and catches an error."""
    print("--- Error/Fault Handling ---")
    try:
        print("Attempting to divide by zero...")
        res = 10 / 0
    
    except ZeroDivisionError as e:
        print(f"CAUGHT ERROR: {e} (You cannot divide by zero).")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    finally:
        print("Error handling block complete. Application is still running.")

    printBlankLines(1)

def main() -> int:
    print("System Monitoring Application Starting")
    print("======================================")
   
    getFileDiskUsageStatistics()   
    getCpuStatistics()
    getMemoryStatistics()
    showThreadingExample()
    showErrorHandling()

    print("======================================")
    print("Program Finished Successfully")
    return 0

if __name__ == '__main__':
    sys.exit(main())
