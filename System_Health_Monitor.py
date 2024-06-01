import psutil
import datetime

# Define thresholds for CPU usage, memory usage, disk space, and number of running processes
CPU_THRESHOLD = 80  # percentage
MEMORY_THRESHOLD = 80  # percentage
DISK_THRESHOLD = 80  # percentage
PROCESS_THRESHOLD = 100  # number of processes

def check_system_health():
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"CPU usage is {cpu_usage}% (threshold: {CPU_THRESHOLD}%)")

    # Get memory usage percentage
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"Memory usage is {memory_usage}% (threshold: {MEMORY_THRESHOLD}%)")

    # Get disk usage percentage of root partition
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"Disk usage is {disk_usage}% (threshold: {DISK_THRESHOLD}%)")

    # Get number of running processes
    num_processes = len(psutil.pids())
    if num_processes > PROCESS_THRESHOLD:
        log_alert(f"Number of running processes is {num_processes} (threshold: {PROCESS_THRESHOLD})")

def log_alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp}: {message}"
    print(log_message)  # Print alert to console
    with open("system_health_alerts.log", "a") as log_file:
        log_file.write(log_message + "\n")  # Log alert to file

if __name__ == "__main__":
    check_system_health()
