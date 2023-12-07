
""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<
def get_shutdown_events(logfile):
    """
    Read the specified log file and return a list of lines where a shutdown was initiated.

    Args:
        logfile (str): The path to the log file.

    Returns:
        list: A list of lines where a shutdown was initiated.
    """
    shutdown_events = []

    try:
        with open(logfile, 'r') as file:
            for line in file:
                if "Shutdown initiated" in line:
                    shutdown_events.append(line.strip())
    except FileNotFoundError:
        print(f"The file {logfile} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return shutdown_events

# Example usage:
logfile_path = "path/to/messages.log"
shutdown_lines = get_shutdown_events(logfile_path)

# The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{shutdown_lines=}")
    if shutdown_lines:
        for line in shutdown_lines:
            print(line)
    else:
        print("No shutdown events found in the log file.")

