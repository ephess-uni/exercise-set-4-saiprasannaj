
""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<
""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<
def get_shutdown_events(logfile):
    shutdown_entries = []

    with open(logfile, 'r') as file:
        for line in file:
            if "Shutdown initiated" in line:
                shutdown_entries.append(line.strip())

    return shutdown_entries

# Example usage:
if __name__ == "__main__":
    try:
        from src.util import get_data_file_path
    except ImportError:
        from util import get_data_file_path

    # Use this FILENAME variable to test your function.
    FILENAME = get_data_file_path('messages.log')

    shutdown_events = get_shutdown_events(FILENAME)

    if shutdown_events:
        for event in shutdown_events:
            print(event)
    else:
        print("No shutdown events found.")
