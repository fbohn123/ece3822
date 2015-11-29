#!/usr/bin/env python
# file: foo.py
# description:

# import the following modules
import os
import sys
import operator
import time
from foo_00 import WordCount

# main
def main(argv):
    # start timer
    tic = time.clock()

    # check command line arguments
    if len(argv) == 1:
        sys.exit("Missing argument(s)")
    # end if

    # initialize and parse command line arguments
    filename = argv[1]
    search_term = argv[2]

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

    # initialize count for the number of file
    num_file = 0
    num_words = 0
    tmp = []
    record = {}
    # loop through every line/path in the txt file
    for path in f:
        # remove the new line characters
        path = path.rstrip("\n")

        # call the readwc method to read the txt files
        db_list = database_obj.readwc(path)

        # count the number files with the search term entered via command line arg
        num_file += database_obj.containsWord(db_list, search_term)[0]
        list_with_word = database_obj.containsWord(db_list, search_term)[1]

        if len(list_with_word) != 0:
            for word in list_with_word:
                if not record.has_key(word):
                    record[word] = 1
                else:
                    record[word] = record[word] + 1
        
    # end for loop

    num_words = database_obj.totalWords(record)
    avg_wpf = float(num_words)/float(num_file)
    database_obj.createHistogram(record,search_term)
    #
    # end timer
    toc = time.clock()

    # calculate the runtime
    runtime = float(toc - tic)

    # display results
    print "A total of %d files contained the word '%s'" %(num_file, search_term)
    print "A total of %d words occurred in %d files: the average words per file is %.2f." %(num_words, num_file, avg_wpf)
    print "Total runtime: %f s" %(runtime)
    # close file(s)
    f.close()
# end main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)
#
# end file
