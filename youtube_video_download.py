from pytube import YouTube
import logging
import re
import os
import requests
import time

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
                time.sleep(2)
                video_title = yt.title
                
                thumbnail_url = yt.thumbnail_url
                #Downloads thumbnail
               
                video_streams = yt.streams.filter(file_extension="mp4", progressive=True)
                VideoDownload.download_thumbnail(thumbnail_url)
                return video_title, thumbnail_url, video_streams
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None, None, None
        else: 
            logging.error(f'{url} is not a Youtube Link')

    def download_thumbnail (thumbnail_url):
        if not os.path.exists('temp'):
            os.makedirs('temp')
        
        temp_filename = os.path.join('temp', "temp.jpg")
        try:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                with open(temp_filename, "wb") as file:
                    file.write(response.content)
                print(f"Thumbnail downloaded and saved as: {temp_filename}")
            else:
                print("Failed to download thumbnail.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        

        

    def download_video(url, quality):
        yt = YouTube(url)
        stream = quality
        stream.download('Downloads')

    
logging.basicConfig(filename='YouTubeVideoDownloader.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    VideoDownload()