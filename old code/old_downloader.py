import os
import time
import argparse
from pytube import YouTube, Playlist
from clip_media import clip_mp4
from mp3convert import convertToMp3

def get_absolute_path(download_path, filename):
    return os.path.abspath(os.path.join(download_path, filename))

def download_video(url, download_path, clip_media=None, convert_to_mp3=False):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video_path = video.download(download_path)
        video_path = get_absolute_path(download_path, video.default_filename)
    except Exception as e:
        with open('errors.log', 'a') as error_file:
            error_file.write(f"Error: {e}. Skipping video: {url}\n")
        return
    if clip_media:
        temp_output_path = get_absolute_path(download_path, "temp_" + os.path.basename(video_path))
        clip_mp4(video_path, temp_output_path, clip_media[0], clip_media[1])
        os.remove(video_path)
        os.rename(temp_output_path, video_path)
    if convert_to_mp3:
        mp3_path = os.path.splitext(video_path)[0] + '.mp3'
        convertToMp3(video_path, mp3_path)
        os.remove(video_path)

def download_playlist(url, download_path=None, limit=None, convert_to_mp3=False):
    playlist = Playlist(url)

    # Apply the limit if specified
    if limit:
        video_urls = playlist.video_urls[:limit]
    else:
        video_urls = playlist.video_urls

    for video_url in video_urls:
        download_video(video_url, download_path, None, convert_to_mp3)

def main():
    parser = argparse.ArgumentParser(description='Download YouTube video or playlist.')
    parser.add_argument('url', help='URL of the YouTube video or playlist.')
    parser.add_argument('-p', '--path', help='Path to the download folder (optional).', default=None)
    parser.add_argument('-l', '--limit', type=int, help='Limit the number of videos to download from a playlist (optional).', default=None)
    parser.add_argument('--clip', action='store_true', help='Clip the downloaded video using the specified start and end times (optional).')
    parser.add_argument("-s", "--start", type=int, default=0, help="Start time (in seconds) to clip from. Default is 0.")
    parser.add_argument("-e", "--end", type=int, default=None, help="End time (in seconds) to clip to. Default is the end of the file.")
    parser.add_argument('--mp3', action='store_true', help='Convert the downloaded video to MP3 format and remove the MP4 file (optional).')

    args = parser.parse_args()

    if "list=" in args.url:
        print("Downloading playlist...")
        if not args.path:
            args.path = '../playlist/'
        download_playlist(args.url, args.path, args.limit, args.mp3)
    else:
        print("Downloading video...")
        clip_media = None
        if not args.path:
            args.path = '..'
        if args.clip:
            clip_media = (args.start, args.end)
        download_video(args.url, args.path, clip_media, args.mp3)

if __name__ == "__main__":
    main()
