# download and change desktop wallpaper automatically

import requests
import json

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

### get the json ###
response = requests.get(api_url)
# print(response)
content = response.content
# print(type(content))

### decode content type bytes from string ###
content = response.content.decode("UTF-8")
# print(type(content))

### convert string to json ###
dict_content = json.loads(content)
# print(dict_content)

### get the image url ###
image_url = dict_content["url"]
# print(image_url)

### download the image ###
res = requests.get(image_url)
# print(res)

### save the image ###
with open("idba_nasa.png", "wb") as image:
    image.write(res.content)
