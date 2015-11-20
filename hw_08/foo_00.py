#!/usr/bin/env python
# file: foo_00.py

# import the following modules
import os
import sys
import re

# class
class WordCount():

    # method: read
    #
    def read(self, filepath):
        # check if the file exists
        words_ls = []
        try:
            # open file
            with open(filepath, 'r') as content_file:
                content = content_file.read()
                content = re.sub("[^A-Za-z0-9']+", ' ', content)
                words_ls = content.rstrip('\r\n').lower().rsplit()
        # end try

        # if not then exit the program
        except:
            print filepath + ": No such file or directory"
            sys.exit()
        # end except

        return words_ls

    # end method read

    # method
    def containsWord(self, words_ls, word):
        count = 0
        if any(word in index for index in words_ls):
            count = 1
        return count
    # end method search

    # method
    def createHistogram():
        pass
    # end method createHistogram
# end class WordCount
