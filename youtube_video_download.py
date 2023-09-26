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
        '''
        Retrieves information about a YouTube video, including its title, thumbnail URL, and available video streams.

        Parameters:
        - url (str): The URL of the YouTube video to retrieve information for.

        This function checks if the provided URL is a valid YouTube link using the `check_url` method from the `VideoDownload` class. If the URL is valid, it proceeds to:
        - Fetch the video's title.
        - Retrieve the thumbnail URL of the video.
        - Download the video's thumbnail using the `download_thumbnail` method from the `VideoDownload` class.
        - Filter and obtain a list of available video streams (progressive MP4 streams) for the video.
        
        If any errors occur during this process, they are logged as errors, and the function returns `None` for all information fields. If the URL is not a valid YouTube link, an error is also logged.

        Returns:
        - video_title (str): The title of the YouTube video.
        - thumbnail_url (str): The URL of the video's thumbnail image.
        - video_streams (list): A list of available video streams for the video, represented as `Stream` objects. If no streams are found, this list is empty.
        '''
        if VideoDownload.check_url(url) == True:
            try:
                yt = YouTube(url)
                #? Short delay added to resolve unable to retrieve error
                time.sleep(2)
                video_title = yt.title
                thumbnail_url = yt.thumbnail_url
                video_streams = yt.streams.filter(file_extension="mp4", progressive=True)
                VideoDownload.download_thumbnail(thumbnail_url)
                return video_title, thumbnail_url, video_streams
            except Exception as e:
                logging.error(f"An error occurred: {str(e)}")
                return None, None, None
        else: 
            logging.error(f'{url} is not a Youtube Link')

    def download_thumbnail (thumbnail_url):
        '''
        Downloads the YouTube video thumbnail as a temporary file.

        Parameters:
        - thumbnail_url (str): The URL of the YouTube video thumbnail image.

        This function fetches the thumbnail image from the provided URL and saves it as a temporary JPG file in the 'temp' folder. If the download is successful, the file path of the saved thumbnail is printed. If any error occurs during the process, an error message is displayed.

        Args:
        - thumbnail_url (str): The URL of the YouTube video thumbnail image.
        '''
        if not os.path.exists('temp'):
            os.makedirs('temp')
        temp_filename = os.path.join('temp', "temp.jpg")
        try:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                with open(temp_filename, "wb") as file:
                    file.write(response.content)
                logging.info(f"Thumbnail downloaded and saved as: {temp_filename}")
            else:
                logging.info('Failed to download thumbnail.')
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

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