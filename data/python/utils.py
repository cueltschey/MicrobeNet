import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO



class Downloader:
    def __init__(self):
        pass

    def download_jpg(self, url, folder_path, filename):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        response = requests.get(url, stream=True)
        with open(os.path.join(folder_path, filename), 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
    def download_gif(self, image_url, folder_path, filename):
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Send a GET request to the image URL
        response = requests.get(image_url)
        
        if response.status_code == 200:
            # Open the image from the response
            gif_image = Image.open(BytesIO(response.content))
            
            # Convert the image to JPEG format
            jpg_image = gif_image.convert("RGB")
            
            # Save the JPEG image to the specified folder path with the provided filename
            jpg_path = os.path.join(folder_path, filename)
            jpg_image.save(jpg_path, "JPEG")
            
            print(f"Conversion completed successfully! Image saved as {jpg_path}")
        else:
            print("Failed to download the image.")

class HTMLParser:
    def __init__(self, html_content):
        self.html_content = html_content
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extract_links(self):
        links = []
        for a_tag in self.soup.find_all('a', href=True):
            link = a_tag['href']
            links.append(link)
        return links
