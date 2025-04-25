import sys
import requests
import socket
import json

# Check if a URL is provided as a command-line argument
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Make a GET request to the provided URL
    req = requests.get(f"https://{url}")
    req.raise_for_status()  # Raise an error for bad responses
    print(f"\nHeaders for {url}:\n{req.headers}")
except requests.RequestException as e:
    print(f"Error fetching URL: {e}")
    sys.exit(1)

try:
    # Resolve the hostname to an IP address
    gethostby_ = socket.gethostbyname(url)
    print(f"\nThe IP address of {url} is: {gethostby_}\n")
except socket.gaierror as e:
    print(f"Error resolving hostname: {e}")
    sys.exit(1)

try:
    # Get location information based on the IP address
    req_two = requests.get(f"https://ipinfo.io/{gethostby_}/json")
    req_two.raise_for_status()  # Raise an error for bad responses
    resp_ = req_two.json()  # Directly parse JSON response

    # Print location and region information
    print(f"Location: {resp_.get('loc', 'N/A')}")
    print(f"Region: {resp_.get('region', 'N/A')}")
except requests.RequestException as e:
    print(f"Error fetching IP info: {e}")
except json.JSONDecodeError:
    print("Error decoding JSON response.")

