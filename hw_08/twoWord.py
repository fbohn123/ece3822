#!/usr/bin/env python
# file: twoWord.py
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
    record = {}
    # loop through every line/path in the txt file
    for path in f:
        # remove the new line characters
        path = path.rstrip("\n")

        # call the readwc method to read the txt files
        db_list = database_obj.readwc(path)

        # list with all tow word sequences -- uncomment to run.
        tw_list = database_obj.twoWordList(db_list)

        # increment the counter for the number of files
        num_file += 1

        # loop through every word in the list and store it in the dictionary record
        for word in tw_list:
            # if the word is not in dictionary store it in the dictionary
            if not record.has_key(word):
                # initialize the new key with a value of 1
                record[word] = 1

            # end if

            # if the word is already in the dictionary
            else:
                # increment the existing count by 1
                record[word] = record[word] + 1
            # end else

        # end for loop

    # end for loop
    
    # compute the total number of words
    num_words = database_obj.totalWords(record)

    # compute the average number of words per file
    avg_wpf = float(num_words)/float(num_file)

    # generate a Histogram
    database_obj.createHistogram(record,search_term)

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
