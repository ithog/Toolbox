import requests
import json
import xml.etree.ElementTree as ET

def test_get_data(base_url, endpoint):
    url = "https://" + base_url + endpoint
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for {url}: {http_err}")
        return
    except Exception as err:
        print(f"Other error occurred for {url}: {err}")
        return
    
    content_type = response.headers.get('Content-Type')
    if 'application/json' in content_type:
        try:
            json_data = response.json()  # Parse JSON
            json_str = json.dumps(json_data, indent=4)
            print(f"API response for {url} (JSON): ", json_str)
        except json.JSONDecodeError:
            print(f"Response content for {url} is not valid JSON")
    elif 'application/xml' in content_type or 'text/xml' in content_type:
        try:
            xml_data = ET.fromstring(response.content)  # Parse XML
            xml_str = ET.tostring(xml_data, encoding='unicode', method='xml')
            print(f"API response for {url} (XML): ", xml_str)
        except ET.ParseError:
            print(f"Response content for {url} is not valid XML")
    elif 'text/plain' in content_type:
        print(f"API response for {url} (Plain Text): ", response.text)
    elif 'text/html' in content_type:
        print(f"API response for {url} (HTML): ", response.text)
    else:
        print(f"Unsupported Content-Type for {url}: {content_type}")

def read_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            endpoints = file.readlines()
        return [endpoint.strip() for endpoint in endpoints]
    except FileNotFoundError:
        print(f"Wordlist file not found: {file_path}")
        return []

def main():
    base_url = input("Enter the base URL for the API: ")
    use_wordlist = input("Do you want to use a wordlist for endpoints? (yes/no): ").strip().lower()

    if use_wordlist == 'yes':
        wordlist_path = input("Enter the path to the wordlist file: ")
        endpoints = read_wordlist(wordlist_path)
        if not endpoints:
            print("No endpoints to test.")
            return
        for endpoint in endpoints:
            test_get_data(base_url, endpoint)
    else:
        endpoint = input("Enter the API endpoint (e.g., /api/users): ")
        test_get_data(base_url, endpoint)

main()
