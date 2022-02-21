# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "http://jsonplaceholder.typicode.com/users"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# get the length of the data_json array
length = len(data_json)

# loop through to pick each city and print
print("List of cities")
for i in range(length):
    print(data_json[i]['address']['city'])
