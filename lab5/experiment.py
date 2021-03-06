#!/usr/bin/python
###################################################################
# CS 423 lab 5 starter code for experiment
# This code should generate two randomly composed DNA sequences of various
# lengths and run the globalAlignment and localAlignment algorithms
# Authors:
####################################################################

import globalAlignment
#import localAlignment   ## comment out once you have this module working

# this is how you call code defined in other files: modulename.functionname
# note that importing globalAlignment above will run the script in its
# entirety, so you may want to comment out any testing code at the bottom
# of that script, so it is not executed prior to the code below
s = "AGAAAAAAAACTA"
t = "TGCATCAAAG"
optimalScore = globalAlignment.globalAlignmentScore(s, t)
print ("Global alignment score: " + str(optimalScore))

# update this code so that it does the following:

# generates randomly composed DNA sequences (25%A, 25%C, 25%T, 25%G)
# of length N and returns it as a string
def randomSeq(N):
    return ""

# runs the following experiment:
# From size Start to Stop going by Step:
#     Generate 2 random DNA strings of length size
#     Calculate the global alignment score between the two strings
#     Calculate the local alignment score between the two strings
#     Write results to file per line
#     such as:
#     5     -4      10
#     where 5 is the length of the two strings, -4 is the optimal
#     global alignment score, and 10 is the optimal local alignment
#     score. Put a newline after each line and separate values per line
#     by tabs. This output file will be used for graphing.
def experiment(Start, Stop, Step, Filename):

    return

# Before running this experiment, be sure that you comment out the
# align function call in globalAlignmentScore, so that files are
# not written with the alignments

# run experiment
experiment(5, 100, 5, "expOutput.txt")
    
