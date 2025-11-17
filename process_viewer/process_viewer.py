"""
process_viewer.py
Displays running system processes using the psutil library.

Author: Malgorzata Debska
Date: 11-17-2025
"""




# Import the necessary library
import psutil

def get_process_info():
    # Get the list of all processes
    processes = psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent'])
    
    # Print header for the output
    print(f"{'PID':<10}{'Process Name':<30}{'Memory Usage (%)':<20}{'CPU Usage (%)':<20}")
    print("-" * 80)
    
    # Retrieve all running processes
    for process in processes:
        try:
            pid = process.info['pid']
            name = process.info['name']
            memory = process.info['memory_percent']
            cpu = process.info['cpu_percent']
            
            # Display process info in a formatted manner
            print(f"{pid:<10}{name:<30}{memory:<20}{cpu:<20}")
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Handle exceptions for processes that have ended or cannot be accessed
            continue

if __name__ == "__main__":
    get_process_info()
