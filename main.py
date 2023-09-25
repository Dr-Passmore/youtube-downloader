import logging

import youtube_video_download
import application_user_interface

class LoadingScript:
    def __init__ (self):
        logging.info('Initising Youtube Download App')
        youtube_video_download.VideoDownload()
        application_user_interface.UserInterface()
        url = "https://www.youtube.com/watch?v=sr3W3XVXVB0&list=RDG8HCJSd_VL4"
        title, thumbnail, streams = youtube_video_download.VideoDownload.get_video_info(url)
        print(title)
        print(thumbnail)
        print("Available Video Quality Options:")
        for stream in streams:
            print(f"Resolution: {stream.resolution}, Format: {stream.mime_type}, File Size: {stream.filesize / (1024 * 1024):.2f} MB")

logging.basicConfig(filename='YouTubeVideoDownloader.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    LoadingScript()