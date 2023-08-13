import argparse
from moviepy.editor import concatenate_videoclips, VideoFileClip

def merge_mp4_files(files, output):
    # Create a list to hold the clips
    clips = []

    # Iterate through the files
    for file in files:
        # Load the mp4 file
        clip = VideoFileClip(file)

        # Add it to the list
        clips.append(clip)

    # Concatenate the clips
    final_clip = concatenate_videoclips(clips)

    # Write the result
    final_clip.write_videofile(output)

def main():
    parser = argparse.ArgumentParser()

    # Add an argument for the files
    parser.add_argument("-f", "--file", action='append', required=True, help="Specify an mp4 file")

    # Add an argument for the output file
    parser.add_argument("-o", "--output", default="merged.mp4", help="Specify the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Merge the files
    merge_mp4_files(args.file, args.output)

if __name__ == "__main__":
    main()
