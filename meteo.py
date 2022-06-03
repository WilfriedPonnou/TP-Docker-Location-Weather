import requests, json, os
 
# Enter your API key here
api_key = str(os.environ.get("API_KEY"))
latitude = str(os.environ.get("LAT"))
longitude = str(os.environ.get("LONG"))
 
# base_url variable to store url
url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}".format(lat=latitude,lon=longitude,API_key=api_key)
 

 
# get method of requests module
# return response object
response = requests.get(url)
 
# json method of response object
# convert json format data into
# python format data
x = response.json()
 
print(x)