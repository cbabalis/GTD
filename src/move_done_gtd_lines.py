#!/usr/bin/python

""" This python script reads a given source file and "clears" it from
    any "DONE" lines, by placing them into another file, given by the
    user.

    In particular, the script is run by giving (from the console):
    - the input file (where the .md with done lines is found)
    - the output file (where the "done" lines will go in) and
    - the string that defines a "done" line (optional).
    If nothing is given, then the script gets "DONE" as the signal to transfer a line.

    Example:

        $ python3 update_GTD3.py NEXT_ACTIONS.md ../LOG/NEXT_ACTIONS_2023.md
        $ python3 update_GTD3.py NEXT_ACTIONS.md ../LOG/NEXT_ACTIONS_2023.md 'DONE'
"""

import sys

def read_file(in_path, out_path, keyword='DONE'):
    """Gets a file and returns it line by line.

    Parameters
    ----------
    in_path: str
        The file location of the input file
    out_path: str
        The file location of the output file
    keyword: str, optional
        A keyword used to indicate if a line will be transferred to
        output file (default is False).

    Returns
    -------
    list
        a list of lines of the file
    """
    # new content is a list with the lines to be written in the old file
    new_content = []
    with open(in_path) as f:
        content = f.read().splitlines()
        for line in content:
            # new_content contains the tasks pending and 0's in the
            # place of tasks that have been done
            new_content.append(process_line(line, out_path, keyword))
    # finally, clean the initial file of the logs
    return new_content

def process_line(a_line, output_file, keyword='DONE'):
    """ Processes a line and sends it either to output file
    or to the original one.

    Parameters
    ----------
    a_line: str
        The line to be processed.
    output_file: str
        The file where the 'DONE' lines go.
    keyword: str, optional
        The keyword based on which the lines go to the
        appropriate file.
    """
    if keyword not in a_line:
        return a_line
    else:
        with open(output_file, "a") as myfile:
            myfile.write((a_line+'\n'))
            myfile.close()
        return 0

def rewrite_input(content, input_file):
    """ Rewrites the initial file with the not done tasks only.

    Parameters
    ----------
    content: str
        Contains the lines not done yet.
    input_file: str
        The original file to populate with not done tasks only.
    """
    with open(input_file, "w") as myfile:
        for line in content:
            if line != 0:
                myfile.write(line+'\n')
        myfile.close()


def main():
    # read input and output files as arguments from command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if len (sys.argv) > 2:
        keyword = sys.argv[-1]
    # load content of file to a var
    content = read_file(input_file, output_file, keyword)
    rewrite_input(content, input_file)

if __name__ == "__main__":
    main()
