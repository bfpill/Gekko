import requests

def write_to_notion(data):
    try:
        payload = {
            "text": data
        }
        response = requests.post("http://localhost:4000/notion_manager/", json=payload)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print("POST request sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}")
