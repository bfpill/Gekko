import json
from datetime import datetime

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


def read_by_date(filename, date):
    # Convert the date to ISO 8601 format (without time)
    date_str = date.isoformat()

    # Read the JSON file
    with open(filename, 'r') as f:
        data = json.load(f)

    # Filter the objects by date
    matching_objects = [obj for obj in data if obj['timestamp'].startswith(date_str)]

    return matching_objects


