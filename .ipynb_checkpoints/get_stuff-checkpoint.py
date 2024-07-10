import os
import glob

# Define the source and destination directories
source_dir = './data/frames_auto_annotate_labels'
dest_dir = './train/labels'

# Get a list of all text files in the source directory
text_files = glob.glob(os.path.join(source_dir, '*.txt'))

# Process each text file
for file_path in text_files:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace "14" with "0" at the start of each line, or discard the line
    new_lines = [line.replace('14', '0', 1) if line.startswith('14') else '' for line in lines]

    # Write the new lines to a file in the destination directory
    dest_file_path = os.path.join(dest_dir, os.path.basename(file_path))
    with open(dest_file_path, 'w') as file:
        file.writelines(new_lines)