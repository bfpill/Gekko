import json
from datetime import datetime
import os

def write_to_json(input_string):
    # Get the current date and format it as a string
    date_str = datetime.now().strftime('%Y-%m-%d')

    # Use the date as the filename
    filename = f"{date_str}.json"

    # Create a dictionary with the string and the current timestamp
    data = {
        "string": input_string,
        "timestamp": datetime.now().isoformat()
    }

    # Write the dictionary to a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f)

def add_to_todo_stack(text):
   write_file_sync("todo_stack.txt", text)

def write_file_sync(filename, data):
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Combine the directory path and filename
    file_path = os.path.join(dir_path, filename)

    try:
        with open(file_path, 'a') as file:
            file.write(data + "\n")
    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"Exception: {e}")

def read_by_date(filename, date):
    # Convert the date to ISO 8601 format (without time)
    date_str = date.isoformat()

    # Read the JSON file
    with open(filename, 'r') as f:
        data = json.load(f)

    # Filter the objects by date
    matching_objects = [obj for obj in data if obj['timestamp'].startswith(date_str)]

    return matching_objects
