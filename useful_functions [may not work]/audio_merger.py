import argparse
from pydub import AudioSegment

def merge_mp3_files(files, gaps, output):
    # Initialize an empty audio segment
    combined = AudioSegment.empty()

    # Iterate through the files and gaps
    for file, gap in zip(files, gaps):
        # Load the mp3 file
        sound = AudioSegment.from_mp3(file)

        # Add it to the combined audio
        combined += sound

        # Generate silence and add it to the combined audio
        silence = AudioSegment.silent(duration=gap*1000)  # gap is in seconds
        combined += silence

    # Save the result (remove the last added silence)
    combined.export(output, format="mp3")

def main():
    parser = argparse.ArgumentParser()

    # Add an argument for the files and gaps
    parser.add_argument("-fg", "--filegap", action='append', required=True, help="Specify a file-gap pair, e.g. 'abc.mp3,2'")

    # Add an argument for the output file
    parser.add_argument("-o", "--output", default="merged.mp3", help="Specify the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Separate the files and gaps
    files = []
    gaps = []
    for filegap in args.filegap:
        file, gap = filegap.split(',')
        files.append(file)
        gaps.append(int(gap))

    # Merge the files
    merge_mp3_files(files, gaps, args.output)

if __name__ == "__main__":
    main()
