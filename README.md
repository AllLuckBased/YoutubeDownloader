***YouTube Video and Playlist Downloader***
This script allows you to download YouTube videos and playlists in the highest resolution available. You can also clip the video to a specific start and end time and convert it to MP3 format.

**Prerequisites**
This script requires Python 3.x and the following Python packages: pytube argparse
You can install these packages by running the following command in your terminal:
pip install pytube argparse

**Usage**
To use this script, you can run the main() function in your Python interpreter or from the command line with the following arguments:
python youtube_downloader.py [-h] [-p PATH] [-l LIMIT] [--clip] [-s START] [-e END] [--mp3] url
*Arguments*
url (required): The URL of the YouTube video or playlist you want to download.
-h, --help: Show the help message and exit.
-p PATH, --path PATH: The path to the download folder (optional). Default is the parent directory of the script.
-l LIMIT, --limit LIMIT: Limit the number of videos to download from a playlist (optional).
--clip: Clip the downloaded video using the specified start and end times (optional).
-s START, --start START: Start time (in seconds) to clip from. Default is 0.
-e END, --end END: End time (in seconds) to clip to. Default is the end of the file.
--mp3: Convert the downloaded video to MP3 format and remove the MP4 file (optional).

**Examples**
*Download a single video:*
python youtube_downloader.py https://www.youtube.com/watch?v=XXXXXXXXXXX

*Download a video and clip it to the first 30 seconds:*
python youtube_downloader.py https://www.youtube.com/watch?v=XXXXXXXXXXX --clip -s 0 -e 30

*Download a playlist:*
python youtube_downloader.py https://www.youtube.com/playlist?list=XXXXXXXXXXX

*Download a playlist and limit the number of videos to 10:*
python youtube_downloader.py https://www.youtube.com/playlist?list=XXXXXXXXXXX -l 10

*Download a playlist, convert all videos to MP3 format, and save them to a specific folder:*
python youtube_downloader.py https://www.youtube.com/playlist?list=XXXXXXXXXXX --mp3 -p /path/