from library import pic_helper
from library import gaw

# Subreddit options
subreddit = 'avaaddams'

gaws = gaw.Gaw()

# File Paths
base_path = 'C:/Users/thoma/Desktop/Data/reddit_downloads/'

ph = pic_helper.PicHelper(base_path, 'testing')

# Download video
urls = ['https://thumbs.gfycat.com/NiftyGracefulIvorygull-mobile.mp4', 
        'https://thumbs.gfycat.com/KaleidoscopicShamefulFalcon-mobile.mp4']

download_dir = ph.download_dir

for url in urls:
    #ph.download_url(url, download_dir)
    pass

# Download gfy
gfys = ['https://gfycat.com/KaleidoscopicShamefulFalcon',
        'https://gfycat.com/NiftyGracefulIvorygull',
        'https://gfycat.com/RevolvingCoordinatedHectorsdolphin']

for gfy in gfys:
    print(gaws.get_mp4_url_from_page_url(gfy))

