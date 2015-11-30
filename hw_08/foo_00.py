#!/usr/bin/env python
# file: foo_00.py

# import the following modules
import os
import sys
import re
import operator
from collections import Counter

class WordCount():

    # method: readwc
    # arguments: filepath - path to each txt file
    # return: a list of every word in the txt file
    #
    def readwc(self, filepath):
        # declare a list
        txt_ls = []

        # check if the file exists
        try:
            # open file
            with open(filepath, 'r') as content_file:
                # read the entire file and store content
                content = content_file.read()

                # remove special characters
                content = re.sub("[^A-Za-z0-9]+", ' ', content)

                # remove new line, make lower case, split word by word into list
                txt_ls = content.rstrip('\r\n').lower().rsplit()
            # end open
        # end try

        # if not then exit the program
        except:
            print filepath + ": No such file or directory"
            sys.exit()
        # end except

        return txt_ls
    # end method readwc

    # method: containsWord
    # arguments: list words_ls, string words
    # return: count = 1 if word is in the list or 0 if it is not
    #
    def containsWord(self, txt_ls, search_term):
        # initialize
        count = 0
        word_ls = []

        # search for any occurrances of the word in the list
        # include an variation of the word
        # ex: 'spikes', if word is 'spike'
        if any(search_term in index for index in txt_ls):
            # set count to 1
            count = 1

            # set the word_ls to txt_ls
            word_ls = txt_ls

        # end if

        # return the count and the list
        return (count, word_ls)
    # end method containsWord


    def totalWords(self, record):
        total = 0
        for word in record:
            total += int(record[word])
        return total

    # method:
    def createHistogram(self, record, search_term):
        # initialize total number of words
        total = 0

        # print heading
        print "-"*(61 + len(search_term))
        print "Histogram of all the word in all files that have the word '%s'." %(search_term)
        print "-"*(61 + len(search_term))

        # compute the total number of words
        total = self.totalWords(record)

        # 
        for word in sorted(record, key=record.get, reverse=True):
            # width is used to space out the word from the percentage
            width = 36 - len(word)

            # compute the percentage
            percentage = float(record[word])/total * 100

            # print out the word and the percentage
            print "%s %s %.6f %%" %(str(word), str(" "*width), percentage )
        # end for loop

    # end createHistogram

    # method:
    # arguments:
    # return:
    #
    def twoWordList(self,txt_ls):
        two_words = []
        for i in range(0,len(txt_ls) - 1):
            two_words.append(txt_ls[i] + " " + txt_ls[i+1])
        return two_words
    # end twoWordList

# end class WordCount
