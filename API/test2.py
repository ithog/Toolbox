import requests
import json
import xml.etree.ElementTree as ET

base_url = input("Enter the base URL for the API: ")
endpoint = input("Enter the API endpoint (e.g., /api/users): ")

def get_request(base_url, endpoint):
    url = "https://" + base_url + endpoint
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return
    except Exception as err:
        print(f"Other error occurred: {err}")
        return
    
    content_type = response.headers.get('Content-Type')
    if 'application/json' in content_type:
        try:
            json_data = response.json()  # Parse JSON
            json_str = json.dumps(json_data, indent=4)
            print("API response (JSON): ", json_str)
        except json.JSONDecodeError:
            print("Response content is not valid JSON")
    elif 'application/xml' in content_type or 'text/xml' in content_type:
        try:
            xml_data = ET.fromstring(response.content)  # Parse XML
            xml_str = ET.tostring(xml_data, encoding='unicode', method='xml')
            print("API response (XML): ", xml_str)
        except ET.ParseError:
            print("Response content is not valid XML")
    elif 'text/plain' in content_type:
        print("API response (Plain Text): ", response.text)
    elif 'text/html' in content_type:
        print("API response (HTML): ", response.text)
    else:
        print(f"Unsupported Content-Type: {content_type}")

get_request(base_url, endpoint)
