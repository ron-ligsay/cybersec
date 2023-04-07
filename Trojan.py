import os
import shutil

# use os.path.expanduser() to get the user's home directory
home_dir = os.path.expanduser("~")

# use os.path.join() to construct the path to the source directory
source_dir = os.path.join(home_dir, 'Pictures')

# use os.path.join() to construct the path to the destination directory
destination_dir = os.path.join(home_dir, 'Desktop')

# get the list of files in the source directory
files = os.listdir(source_dir)

# iterate through the list of files
for file in files:
    # check if the file is a .jpg file
    if file.endswith('.jpg'):
        # use shutil.copy2() to copy the file to the destination directory
        shutil.copy2(os.path.join(source_dir, file), destination_dir)
