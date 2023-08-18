import sys
from GTD import GTD

def main():
    # read input and output files as arguments from command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if len (sys.argv) > 2:
        keyword = sys.argv[-1]
    GTD(input_file, output_file)

if __name__ == "__main__":
    main()
