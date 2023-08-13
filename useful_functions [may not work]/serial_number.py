import os
import stat
import time

def get_creation_time(file_path):
    # Get the creation time of the file in seconds since the epoch
    return os.stat(file_path)[stat.ST_CTIME]

def add_serial_numbers_sorted(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a valid directory.")
        return

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Filter out directories and get the creation time for each file
    file_info_list = [(file, get_creation_time(os.path.join(folder_path, file))) for file in file_list if not os.path.isdir(os.path.join(folder_path, file))]

    # Sort the file list based on creation time (ascending order)
    file_info_list.sort(key=lambda x: x[1])

    # Initialize a serial number counter
    serial_number = 1

    for filename, _ in file_info_list:
        # Create a new filename with the serial number prefix
        new_filename = f"{serial_number:03d}. {filename}"
        #print(new_filename)
        
        # Get the full path of the old and new filenames
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        # Rename the file with the new filename
        os.rename(old_path, new_path)

        # Increment the serial number for the next file
        serial_number += 1
        
def undo_rename(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    for filename in file_list:
        # Check if the file has the correct prefix format (e.g., "001_")
        if len(filename) > 4 and filename[4] == ' ' and filename[:3].isdigit():
            # Remove the first four characters (including the underscore)
            new_filename = filename[5:]
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file with the new filename to undo the renaming
            os.rename(old_path, new_path)
        else:
            print(filename[4])

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    add_serial_numbers_sorted(folder_path)
    #undo_rename(folder_path)
    print("Serial numbers have been added to the filenames in the folder, sorted by creation date.")
