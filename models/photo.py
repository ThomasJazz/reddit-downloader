import os
import sys
import hashlib
from PIL import Image

class Photo:
    def __init__(self, file):
        extensions = {'.jpg', '.jpeg', '.png'}
        self.extension = os.path.splitext(file)[1]

        # Validate filetype
        if not(self.extension in extensions):
            raise 'Invalid file type'

        # Metadata
        self.path = file
        self.name = os.path.basename(file)
        self.hash = self.get_hash(file)
        self.width, self.height = self.get_dimensions(file)
        self.size_kb = os.path.getsize(file)
        

    def get_hash(self, file: str):
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    

    def get_dimensions(self, file: str):
        with Image.open(file) as im:
            return im.size
    
    def to_string(self):
        return str(self.__dict__)


    
            