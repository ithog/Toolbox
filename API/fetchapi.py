import requests  # Library för HTTP requests
import json

def fetch_api(url):  # Skapar en funktion
    response = requests.get(url)
    if response.status_code == 200:
        json_response = json.dumps(response.json(), indent=4)  # Skapar en variabel för mer läsbar output
        print(f"API response from {url} (JSON):\n{json_response}")
    else:
        print(f"Failed to fetch data from {url}, status code: {response.status_code}")  # Om statuskoden inte är 200

base_url = input("Enter the base URL: ")
use_wordlist = input("Do you want to use a wordlist for endpoints? (yes/no): ").lower()

if use_wordlist == 'yes':
    wordlist_file = input("Enter the path to the wordlist file: ")

    try:
        with open(wordlist_file, 'r') as file:
            endpoints = file.readlines()
            for endpoint in endpoints:
                endpoint = endpoint.strip()
                url = base_url + endpoint
                fetch_api(url)
    except FileNotFoundError:
        print(f"The file {wordlist_file} does not exist.")
else:
    endpoint = input("Enter the API endpoint: ")
    url = base_url + endpoint
    fetch_api(url)