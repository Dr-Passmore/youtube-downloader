from pytube import YouTube
import logging
import re
import os
import requests
import time


class VideoDownload():

    def __init__(self):
        """
        Initialise the VideoDownload class.
        """
        logging.info('VideoDownload')

    def check_url(url):
        '''
        Checks if a given URL is a valid YouTube link.

        Parameters:
        - url (str): The URL to be checked.

        This function uses a regular expression pattern to determine if
        the provided URL matches the format of a valid YouTube link. The
        pattern verifies if the URL starts with "http://", "https://",
        "www.youtube.com/", or "youtu.be/" followed by additional
        characters. If the URL matches this pattern, it is considered a
        valid YouTube link, and the function returns `True`. Otherwise,
        it returns `False`.

        Returns:
        - is_valid (bool): `True` if the URL is a valid YouTube link,
        `False` otherwise.
        '''
        youtube_pattern = (
            r'(https?://)?'
            r'(www\.)?'
            r'(youtube\.com|youtu\.be|m\.youtube\.com)/.+'
        )
        # r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$'
        match = re.match(youtube_pattern, url)
        if match:
            return True
        else:
            return False

    def get_video_info(url):
        '''
        Retrieves information about a YouTube video, including its
        title, thumbnail URL, and available video streams.

        Parameters:
        - url (str): The URL of the YouTube video to retrieve
        information for.

        This function checks if the provided URL is a valid YouTube link
        using the `check_url` method from the `VideoDownload` class. If
        the URL is valid, it proceeds to:
        - Fetch the video's title.
        - Retrieve the thumbnail URL of the video.
        - Download the video's thumbnail using the `download_thumbnail`
        method from the `VideoDownload` class.
        - Filter and obtain a list of available video streams
        (progressive MP4 streams) for the video.

        If any errors occur during this process, they are logged as
        errors, and the function returns `None` for all information
        fields. If the URL is not a valid YouTube link, an error is also
        logged.

        Returns:
        - video_title (str): The title of the YouTube video.
        - thumbnail_url (str): The URL of the video's thumbnail image.
        - video_streams (list): A list of available video streams for
        the video, represented as `Stream` objects. If no streams are
        found, this list is empty.
        '''
        if VideoDownload.check_url(url) is True:
            attempts = 5
            video_title = None
            try:
                while attempts > 0:
                    if video_title is None:
                        yt = YouTube(url)
                        time.sleep(2)
                        video_title = yt.title
                        thumbnail_url = yt.thumbnail_url
                        video_streams = yt.streams.filter(
                            file_extension="mp4",
                            progressive=True
                            )
                        VideoDownload.download_thumbnail(thumbnail_url)
                        attempts = attempts - 1
                    else:
                        break
                logging.info(f'Successfull retrieved information for the
                             {video_title}')
                return video_title, thumbnail_url, video_streams

            except Exception as e:
                logging.error(f"An error occurred: {str(e)}")
                return None, None, None
        else:
            logging.error(f'{url} is not a Youtube Link')

    def download_thumbnail(thumbnail_url):
        '''
        Downloads the YouTube video thumbnail as a temporary file.

        Parameters:
        - thumbnail_url (str): The URL of the YouTube video thumbnail
        image.

        This function fetches the thumbnail image from the provided URL
        and saves it as a temporary JPG file in the 'temp' folder. If
        the download is successful, the file path of the saved thumbnail
        is printed. If any error occurs during the process, an error
        message is displayed.

        Args:
        - thumbnail_url (str): The URL of the YouTube video thumbnail
        image.
        '''
        if not os.path.exists('temp'):
            os.makedirs('temp')
        temp_filename = os.path.join('temp', "temp.jpg")
        try:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                with open(temp_filename, "wb") as file:
                    file.write(response.content)
                logging.info(f"Thumbnail downloaded and saved as:
                             {temp_filename}")
            else:
                logging.info('Failed to download thumbnail.')
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")

    def download_video(url, quality):
        '''
        Downloads a video from YouTube using the provided video stream
        quality and saves it to the 'Downloads' folder.

        Parameters:
        - url (str): The URL of the YouTube video to download.
        - stream (Stream): The chosen video stream quality to download
        (e.g., <Stream: itag="22" mime_type="video/mp4" res="720p"
        fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2"
        progressive="True" type="video">).

        This function downloads a video from YouTube using the provided
        URL and the specified video stream quality, which should be a
        `Stream` object containing information about the video stream.
        The video is saved to the 'Downloads' folder. The function uses
        the `pytube` library to handle the download process.

        Args:
        - url (str): The URL of the YouTube video.
        - stream (Stream): The chosen video stream quality.

        Example usage:
        stream_info = <Stream: itag="22" mime_type="video/mp4"
        res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2"
        progressive="True" type="video">
        download_video("https://www.youtube.com/watch?v=VIDEO_ID",
        stream_info)

        Note:
        - Ensure the 'pytube' library is installed to use this function.
        - The downloaded video will be saved in the 'Downloads' folder
        with the original video's title as the filename.
        '''
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
