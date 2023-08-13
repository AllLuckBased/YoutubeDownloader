import argparse
from pydub import AudioSegment

def join_mp3_files(file1_path, file2_path, output_file_path):
    # Load the MP3 files using pydub's AudioSegment
    audio1 = AudioSegment.from_mp3(file1_path)
    audio2 = AudioSegment.from_mp3(file2_path)

    # Concatenate the two audio segments
    joined_audio = audio1 + audio2

    # Export the joined audio to a new MP3 file
    joined_audio.export(output_file_path, format="mp3")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Join 2 mp3 audio files.')
    parser.add_argument('file1', metavar='file1', type=str,
                        help='path to first audio file')
    parser.add_argument('file2', metavar='file2', type=str,
                        help='path to second audio file')
    parser.add_argument('output_path', metavar='output_path', type=str,
                        help='path to output MP3 audio file')

    # Parse command line arguments
    args = parser.parse_args()

    join_mp3_files(args.file1, args.file2, args.output_path)
    print("MP3 files joined successfully.")
