import requests

loc = "https://sheets.googleapis.com/v4/spreadsheets/1-6NL6sZIC4XcbwE7BsZYLBBoeByvZNeqhyFKm15X6ls/values/Monolith?key=AIzaSyBBY5QhOXZfkTp_Y8828C00ad7Gf6NTdgQ"
header = {"content-type": "application/json"}
r = requests.get(loc, headers=header)
print(r.json())