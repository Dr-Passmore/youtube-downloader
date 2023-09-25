from pytube import YouTube
import logging
import re

class VideoDownload:
    def __init__ (self):
        logging.info('VideoDownload')

       
    def check_url (url):
        youtube_pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'
        
        match = re.match(youtube_pattern, url)
        
        if match:
            return True
        else:
            return False

    def get_video_info (url):
        if VideoDownload.check_url(url) == True:
            try:
                yt = YouTube(url)
                video_title = yt.title
                #thumbnail_url = yt.thumbnail_url
                return video_title#, thumbnail_url
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None, None
        else: 
            logging.error(f'{url} is not a Youtube Link')

    #def download_video(url, quality):
        
    

    
logging.basicConfig(filename='YouTubeVideoDownloader.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    VideoDownload()