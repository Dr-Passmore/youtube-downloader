import logging

import youtube_video_download

class LoadingScript:
    def __init__ (self):
        logging('Initising Youtube Download App')
        youtube_video_download.VideoDownload()

logging.basicConfig(filename='YouTubeVideoDownloader.log', 
                    filemode='a', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    LoadingScript()