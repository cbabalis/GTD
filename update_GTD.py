#!/usr/bin/python

""" This python script reads a given source file and "clears" it from
    any "DONE" lines, by placing them into another file, given by the
    user.
"""

import sys

def read_file(in_path,out_path, keyword='DONE'):
    """ This method reads a file and returns it.
    @param in_path is the path of the file to be read.
    @param out_path is the path of the file to be written (log file)
    @return my_file
    """
    # new content is a list with the lines to be written in the old file
    new_content = []
    # opens the file
    with open(in_path) as f:
        content = f.read().splitlines()
        for line in content:
            # new_content contains the tasks pending and 0's in the 
            # place of tasks that have been done
            new_content.append(process_line(line, out_path))
    # finally, clean the initial file of the logs
    rewrite_input(new_content, in_path)

def process_line(aline, output_file, keyword='DONE'):
    """ This method processes a line and adds it to the appropriate
    file. If a 'DONE' keyword is in it, then it adds the line to the
    output file and deletes it from the original file. 
    Else, it leaves it to the original file.
    @param aline is the current line
    @param keyword is the keyword due to which the split is taking
    place. Default word is DONE.
    """
    # split the line to words
    words = aline.split(" ")
    # check if 'DONE' keyword exists into the words
    if keyword not in words:
        return aline
    else:
        # if keyword exists, then write the line to new file
        with open(output_file, "a") as myfile:
            myfile.write((aline+'\n'))
            myfile.close()
        return 0

def rewrite_input(content, input_file):
    """ This method populates the input file only with the lines that
    describe tasks pending/not done.
    @param content is the content to be written
    """
    with open(input_file, "w") as myfile:
        for line in content:
            if line != 0:
                myfile.write(line+'\n')
        myfile.close()

def print_msg(msg, vrble):
    # prints the message and the variable
    print msg + " " + vrble

def main():
    # read input and output files as arguments from command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if len (sys.argv) > 2:
        keyword = sys.argv[-1]
    read_file(input_file, output_file)

if __name__ == "__main__":
    main()
