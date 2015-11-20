#!/usr/bin/env python
# file: create_list.py
# description: loop over all *.txt files in the example database

# import the following modules
import os
import sys

# main
def main(argv):
    """ Traverses through a directory and search for all .*txt files and stores the full path to the .txt in an output file.
    Usage: python foo.py <target> <output file> """
    #
    my_path = argv[1]
    output_file = argv[2]

    # open the output file with write permission
    f = open(output_file, "w")

    # loop over every directory
    for root, dirs, files in os.walk(my_path):
        for file in files:
            if file.endswith(".txt"):
                txt_path = os.path.join(root, file)
                f.write(txt_path + '\n')
            # end if
        # end for
    # end for

    # close file
    f.close()
# end main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)
#
# end file
