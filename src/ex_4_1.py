""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<
from ex_4_0 import get_shutdown_events

def num_shutdowns(logfile):
    """
    Count and return the number of shutdowns present in the specified log file.

    Args:
        logfile (str): The path to the log file.

    Returns:
        int: The number of shutdowns present in the file.
    """
    shutdown_events = get_shutdown_events(logfile)

    # Counting shutdown events (each event has "Shutdown initiated" and "Shutdown complete" entries)
    num_shutdowns = len(shutdown_events) // 2

    return num_shutdowns

# Example usage:
if __name__ == "__main__":
    logfile_path = "path/to/messages.log"
    shutdown_count = num_shutdowns(logfile_path)
    print(f"Number of shutdowns: {shutdown_count}")
