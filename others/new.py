# Download and change desktop wallpaper automatically
# pip install requests
# pip install PyWallpaper

import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Get the JSON
response = requests.get(api_url)
content = response.content.decode("UTF-8")

# Convert string to JSON
dict_content = json.loads(content)

# Get the image URL
image_url = dict_content["url"]

# Download the image
res = requests.get(image_url)

# Save the image
image_path = r"C:\Users\NOMAN\Desktop\New folder\idba_nasa.png"
with open(image_path, "wb") as image:
    image.write(res.content)

# Set wallpaper
PyWallpaper.change_wallpaper(image_path)
