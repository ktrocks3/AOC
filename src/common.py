import datetime
import os  # Import os module to work with directories

# Get the current year and the day difference
year = datetime.datetime.today().year
day = (datetime.datetime.today() - datetime.datetime(2024, 12, 1)).days + 1

# Create the directory if it doesn't exist
directory = f'{year}/star{day}'
os.makedirs(directory, exist_ok=True)

# Now, open the file and write to it
file_path = f'{directory}/star{day}.py'
with open(file_path, 'w') as f:
    f.write(''.join(open('template').readlines()))
