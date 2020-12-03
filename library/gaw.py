import requests

class Gaw:
    def __init__(self):
        self.client_id = '2_N9jeEX'
        self.client_secret = 'bmWJlEj8IIo1fP3zOvs1X6Pf3QhNJhVY5Tl0o6AsXXnBV-QQ_Gy1LpoE3OHM40ws'
        self.get_url = 'https://api.gfycat.com/v1/gfycats/{gfy_id}'
    
    # Get URL with extension
    def get_mp4_url(self, gfy_id: str):
        try:
            temp_url = self.get_url.replace('{gfy_id}', gfy_id)
            r = requests.get(url=temp_url)
            return r.json()['gfyItem']['mp4Url']
        except:
            raise Exception(f'ERROR, could not get mp4 url from gfy: {gfy_id}')
    
    # Get URL based on the page URL
    def get_mp4_url_from_page_url(self, url):
        try:
            gfy_id = self.get_gfy_id(url)
            return self.get_mp4_url(gfy_id)
        except:
            raise Exception(f'ERROR, could not get mp4 from url: {url}')


    def get_gfy_id(self, url):
        return url.split('/')[-1]