import os
import sys
import hashlib
import urllib.request
from urllib.parse import urlparse
import pickle

from models import photo
from library import gaw

class PicHelper:
    def __init__(self):
        # Set up config directories
        self.root_dir = os.path.dirname(sys.argv[0])
        self.cfg_dir = self.join(self.root_dir, 'config')
        
        self.history_dir = self.join(self.root_dir, 'history')
        self.history_ext = '.dat'

        # Set of valid extensions
        self.extensions = {'.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm'}

        # Gfycat API wrapper
        self.gaws = gaw.Gaw()
    

    def join(self, parent, child):
        return os.path.join(parent, child).replace('\\', '/')
    

    def create_dir(self, folder):
        if not(os.path.exists(folder)):
            os.mkdir(folder)
    

    # Informational Functions
    def has_extension(self, url):
        index = url.rfind('.')
        if index == -1:
            return False

        extension = url[index:]
        return extension in self.extensions
    

    def get_extension(self, url):
        index = url.rfind('.')
        if index == -1:
            return None

        extension = url[index:]

        if extension in self.extensions:
            return extension
        else:
            return None


    def get_photo_obj(self, file):
        return photo.Photo(file)

    def download_url(self, url, download_dir):
        file_path = os.path.basename(url)
        file_path = self.join(download_dir, file_path)
        if (os.path.exists(file_path)):
            print(f'File {file_path} already exists. Skipping...')
            return
            
        print(f'Downloading {url} -> {file_path}...')
        urllib.request.urlretrieve(url, file_path)

    
    #################################
    ############ HISTORY ############
    #################################
    def get_history(self, subreddit):
        file_path = self.history_dir + subreddit + self.history_ext

        if not(os.path.exists(file_path)):
            return set()

        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            return data
    
    def update_history(self, subreddit, data):
        file_path = self.history_dir + subreddit + self.history_ext

        with open(file_path, 'wb') as file:
            pickle.dump(data, file)