"""
system_info.py
-----------------
A Python program that retrieves and displays high-level CPU and memory
information using the psutil library.

Author: Malgorzata Debska
Date: 12/01/2025
CS-510
"""

import psutil  # psutil provides functions to access system information


def display_cpu_info():
    """
    Retrieves and prints CPU usage and CPU count information.
    """
    cpu_usage = psutil.cpu_percent(interval=1)  # percentage of CPU usage over 1 second
    cpu_count = psutil.cpu_count(logical=True)  # total number of logical CPU cores

    print("----- CPU Information -----")
    print(f"CPU Usage Percentage: {cpu_usage}%")
    print(f"CPU Count (Logical Cores): {cpu_count}")
    print()


def display_memory_info():
    """
    Retrieves and prints memory usage information.
    """
    memory = psutil.virtual_memory()  # returns stats about system memory
    total_memory = round(memory.total / (1024 ** 3), 2)  # convert bytes to GB
    used_memory = round(memory.used / (1024 ** 3), 2)
    memory_percent = memory.percent  # percent of memory in use

    print("----- Memory Information -----")
    print(f"Total Memory Available: {total_memory} GB")
    print(f"Used Memory: {used_memory} GB")
    print(f"Memory Usage Percentage: {memory_percent}%")
    print()


def main():
    """
    Main function that calls the CPU and memory display functions.
    """
    print("System Resource Information")
    print("============================")
    display_cpu_info()
    display_memory_info()


if __name__ == "__main__":
    main()
