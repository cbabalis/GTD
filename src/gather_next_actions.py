""" This script searches all the folders and the subfolders for any
    NEXT_ACTIONS files and gathers their content in a single
    NEXT_ACTIONS.txt file.
    Its input is the root (from which the script recursively will look
    in each folder in order to find all NEXT_ACTIONS files.
"""

import os
import sys

# read the root directory as input from the user
rootdir = sys.argv[1]
# and define a keyword based on which the search is taking place.
keyword = 'NEXT_ACTIONS'

# now open the file
with open('NEXT_ACTIONS.txt', 'w') as dest:
    for directory, subdir, files in os.walk(rootdir):
        for filename in files:
            # ignore other files, just copy contents of the files
            # that contain the keyword in their name
            if keyword in filename:
                with open(os.path.join(directory, filename), 'r') as src:
                    dest.write(src.read())

