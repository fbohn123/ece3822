#!/usr/bin/env python
# file: foo.py
# description:

# import the following modules
import os
import sys
from foo_00 import WordCount

# main
def main(argv):
    # check command line arguments
    if len(argv) == 1:
        sys.exit("Missing argument(s)")
    # end if

    filename = argv[1]
    word = argv[2]

    try:
        # open file
        f = open(filename, "r")
    # end try

    # if not then exit the program
    except:
        print filename + ": No such file or directory"
        sys.exit()

    # create object
    database_obj = WordCount()

    num_file = 0
    #
    for path in f:
        path = path.rstrip("\n")
        db_list = database_obj.read(path)
        num_file += database_obj.containsWord(db_list, word)
    print "A total of %d files contained the word '%s'" %(num_file, word)
    f.close()
# end main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)
#
# end file
