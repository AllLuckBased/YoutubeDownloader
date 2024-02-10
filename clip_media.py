import argparse
from pydub import AudioSegment
from moviepy.video.io.VideoFileClip import VideoFileClip

def clip_mp3(input_path, output_path, start_time, end_time):
    audio = AudioSegment.from_mp3(input_path)
    start_ms = start_time * 1000
    end_ms = end_time * 1000 if end_time is not None else len(audio)
    clipped_audio = audio[start_ms:end_ms]
    clipped_audio.export(output_path, format="mp3")
    
def clip_mp4(input_path, output_path, start_time, end_time):
    video = VideoFileClip(input_path)
    start_seconds = start_time
    end_seconds = end_time if end_time is not None else video.duration
    clipped_video = video.subclip(start_seconds, end_seconds)
    clipped_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    video.close()

def main():
    parser = argparse.ArgumentParser(description="Clip an MP3 file.")
    parser.add_argument("input_path", help="Path to the input file.")
    parser.add_argument("output_path", help="Path to save the clipped file.")
    parser.add_argument("-s", "--start", type=int, default=0, help="Start time (in seconds) to clip from. Default is 0.")
    parser.add_argument("-e", "--end", type=int, default=None, help="End time (in seconds) to clip to. Default is the end of the file.")
    args = parser.parse_args()

    clip_mp4(args.input_path, args.output_path, args.start, args.end)
    
if __name__ == "__main__":
    main()
