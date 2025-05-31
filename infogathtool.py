import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

gethostby_ = socket.gethostbyname(sys.argv[1])
print("The IP Address of the website " + sys.argv[1] + " is: " + gethostby_)

req_api = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
api_res = json.loads(req_api.text)

print("The IP Address " + gethostby_ + " belongs to: " + api_res['org'])
print("The IP Address " + gethostby_ + " is located at: " + api_res['city'] + ", " + api_res['region'] + ", " + api_res['country'] + ", " + api_res['postal'])
print("The IP Address " + gethostby_ + " geological coordinates are: " + api_res['loc'])
