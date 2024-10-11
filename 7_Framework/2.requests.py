import json
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python 2.requests.py <Search_term>")
    sys.exit() #exists  the loop if searchterm is empty

url = f"https://itunes.apple.com/search?entity=song&limit=40&term=" #the &limit=50 limits song results to 50 and you may change to any limit

response = requests.get(url + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
json_output = response.json()
for result in json_output["results"]:
    print(f"{result["trackName"]} recoreded and produced by {result["artistName"]}") # for every loop it displays the trackName and artistName