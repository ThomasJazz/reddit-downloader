import praw             # Reddit API Wrapper
import urllib.request
from urllib.parse import urlparse
import os.path
import time

from library import pic_helper
from library import gaw
# TODO:
# - Build model for subreddit config
# - Build driver class that will handle user input and multiple menus (editing config, downloading pics, etc)
# - Build model for lists of subreddits that share config options (download path)

################################
############ Config ############
################################
# API Info
user_agent = 'Photo Downloader for Reddit v0.1 (by rozcz01)'
client_id = '4Oz93PGCblXdRQ'
client_secret = 'DrvTqeQ0hjGSkY4dE7bIMVLOtI8'

# Subreddit options
subreddits = ['vscosluts', 'jizzedtothis']

# Number of posts to scan through
num_posts = 30

# File Paths
base_path = 'C:/Users/thoma/Desktop/Data/reddit_downloads/'

# helper objects
ph = pic_helper.PicHelper()

# API Wrappers
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
gfycat = gaw.Gaw()

# Website data
image_sites = {'i.imgur.com', 'gfycat.com', 'i.redd.it'}

# Types of content supported
extensions = {'.jpg', '.jpeg', '.png', '.mp4', '.webm', '.gif'}



# Historical download data
dl_history = set()

#####################################
############# Functions #############
#####################################
# Retrieve post urls from the subreddit
def get_urls(subreddit):
    print('Getting post urls...')
    urls = set()

    # Get post URLS
    for submission in reddit.subreddit(subreddit).
    for submission in reddit.subreddit(subreddit).top(limit=num_posts):
        url = submission.url
        extension = ph.get_extension(url)

        if ('gfycat.com' in url):
            try:
                url = gfycat.get_mp4_url_from_page_url(url)
            except Exception as e:
                url = None
                print(e)
        elif ('//imgur' in url):
            url = url.replace('imgur', 'i.imgur')
            url = url + '.jpg'
        elif not(extension in extensions):
            url = None
        
        # Make sure we haven't previously downloaded this link
        if (url and url not in dl_history):
            urls.add(url)
    
    return urls


################################
############# Body #############
################################
for subreddit in subreddits:
    # Folder to download to
    download_dir = f'{base_path}{subreddit}/'

    dl_history = ph.get_history(subreddit)
    url_set = get_urls(subreddit)

    # Download all the images from our url list
    for url in url_set:
        file_path = os.path.basename(url)
        file_path = ph.join(download_dir, file_path)
        extension = ph.get_extension(url)
        
        try:
            ph.download_url(url, download_dir)
            time.sleep(.5)
        except Exception as e:
            print(f'\tError: {e}')

    dl_history = dl_history.union(url_set)
    ph.update_history(subreddit, dl_history)
    
'''


download_dir = 'C:/Users/thoma/Desktop/Data/reddit_downloads/'
url = 'https://i.redd.it/0c61ghgmvb101.jpg'
file_path = os.path.basename(url)
file_path = os.path.join(download_dir, file_path)



'''