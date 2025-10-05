# Import
import re

# Regex
pattern = r"(WARNING|ERROR)"

# Path to the log file
log_file_path = "/var/log/syslog"

# Open and read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        # Search for lines containing WARNING or ERROR
        if re.search(pattern, line):
            print(line.strip())  # Print the matching line, stripping whitespace

