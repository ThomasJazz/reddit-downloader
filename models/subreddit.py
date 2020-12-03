import sys
import os
import json

class Subreddit():
    def __init__(self, name):
        self.name = name
        self.download_dir = None

        # Download options
        self.download_pics = True
        self.download_vids = True
    
    def set_dir(self, directory):
        self.download_dir = directory + self.name
    
    def set_download_pics(self, option: str):
        if (option.lower() == 'y'):
            self.download_pics = True
        elif (option.lower() == 'n'):
            self.download_pics = False
        else:
            raise 'Error, please use y/n'

        self.download_pics = option
    
    def set_download_vids(self, option: str):
        if (option.lower() == 'y'):
            self.download_vids = True
        elif (option.lower() == 'n'):
            self.download_vids = False
        else:
            raise 'Error, please use y/n'

        self.download_pics = option

    def get_json(self):
        json_dict = {
            'name': self.name,
            'download_dir': self.download_dir,
            'download_pics': self.download_pics,
            'download_vids': self.download_vids
        }

        return json.dumps(json_dict)

    