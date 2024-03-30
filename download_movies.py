import requests
import os
import time

def download_file(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
        #print("Downloading", url)
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully: {filename}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    
    except:
            print("Ignoring this movie")

