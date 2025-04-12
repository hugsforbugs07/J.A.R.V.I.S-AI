import replicate
import webbrowser
import requests
import io 
import os
from PIL import Image

# Set your Replicate API token here
REPLICATE_API_TOKEN = "r8_6kB0o2ibXnVW9qfXN8rHkdB9ACRWOtX43shR0"  # TODO: Replace with your actual token

# Initialize Replicate client
replicate.Client(api_token=REPLICATE_API_TOKEN)

def generate_image(prompt):
    try:
        output = replicate.run(
            "stability-ai/sdxl:5c231360b871d27e636c5b2f7b2c8916d77aa843c05c5e6f503579e6e6b98c2c",
            input={"prompt": prompt}
        )
        return output[0]
    except Exception as e:
        print("Error generating image:", e)
        return None

# Calling the function with prompt
image_url = generate_image("a boy making a coding project")

# Downloading and saving the image
if image_url:
    data = requests.get(image_url).content
    with open("img.jpg", "wb") as f:
        f.write(data)
    # Opening the image in browser
    webbrowser.open(image_url)
else:
    print("Image generation failed.")
