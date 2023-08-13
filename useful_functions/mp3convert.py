import argparse
from moviepy.editor import *

# Convert video to audio
def convertToMp3(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)

    # Clean up
    video.close()
    audio.close()
    
def convert_webm_audio_to_mp3(input_file_path, output_file_path):
    # Load the WebM file (treat it as an audio file)
    audio = AudioFileClip(input_file_path)

    # Save the audio as an MP3 file
    audio.write_audiofile(output_file_path)

    # Close the audio object
    audio.close()
    
def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Convert video to MP3 audio')
    parser.add_argument('input_path', metavar='input_path', type=str,
                        help='path to input video file')
    parser.add_argument('output_path', metavar='output_path', type=str,
                        help='path to output MP3 audio file')

    # Parse command line arguments
    args = parser.parse_args()
    convertToMp3(args.input_path, args.output_path)
    
if __name__ == "__main__":
    main()
