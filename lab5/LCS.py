#!/usr/bin/python# Caleb Piekstra and Sara Perkins# CS 423, Lab 5# fall 2015##################################################################### convertFileToSequence - takes a FASTA file and returns the# sequence as a string#####################################################################def convertFileToSequence(filename):    # read in file    file = open(filename)    # read in first line    header = file.readline()    if (header[0] == '>'):        print("in FASTA format")    else:        print("invalid format")        file.close()        return      # read in rest of file    sequence = file.read()        # close file    file.close()    # remove all return and newline characters    sequence = sequence.replace("\r", "")    sequence = sequence.replace("\n", "")    return sequence    ####################################################################### LCSScore - Determines the score of the optimal alignment of # two strings (s1 and s2)######################################################################def LCSScore(s1, s2, filename=None):     # add a blank string as padding     s1 = ' ' + s1     s2 = ' ' + s2     # set table size     NUM_ROWS = len(s2)     NUM_COLS = len(s1)     # Create table and fill it with zeros     c = createTable(NUM_ROWS, NUM_COLS, 0)     # Creates table for getting back the optimal alignment, fill table with "F"     # uses "D", "L", and "T" for diagonal, left, and top     d = createTable(NUM_ROWS, NUM_COLS, "F")     # The above automatically sets the gap penalties in left column and top row          # implements dynamic programming algorithm for LCS     # fills in entries in cost table and direction table          # update table to show alignment penalties     for i in range(1, NUM_ROWS):          for j in range(1, NUM_COLS):               # calculate costs based on direction               left = c[i][j-1]               top = c[i-1][j]               diag = c[i-1][j-1] + 1               # set cost               if s1[j] == s2[i]:                    cost = max(left, top, diag)               else:                    cost = max(left, top)                              c[i][j] = cost               # set direction based on cost               # Precedence: L > T > D                            if cost == left:                    d[i][j] = "L"               elif cost == top:                    d[i][j] = "T"               else:                    d[i][j] = "D"                    # Prints out table (only useful for small tables - used for debugging)     # Commented out, satisfied that the algorithm is working     # printTable(c, "costs.txt")     # printTable(d, "directions.txt")     # find optimal alignment     if filename:        align(d, s1, s2, filename)     else:        align(d, s1, s2, "alignment.txt")     # return optimal score (lower right-hand cell in table]     return c[NUM_ROWS-1][NUM_COLS-1]##################################################################### Creates a 2D table with the given number of rows and columns# and fills all entries with value given as a parameter# (function completed by Tammy VanDeGrift)####################################################################def createTable(numRows, numCols, value):     table = []     row = 0     # create 2D table initialized with value     while (row < numRows):          table.append([])          col = 0          while (col < numCols):               table[row].append(value)               col = col + 1          row = row + 1     return table################################################################### Prints 2D table to file (only useful for small tables for short# strings), can be used for integer as well as char values# tabs between the values on each row# Useful function for debugging purposes only##################################################################def printTable(table, filename):     NUM_ROWS = len(table)     NUM_COLS = len(table[0])     # write table to output file, one row at a time     with open(filename, 'w') as out:          for i in range(0, NUM_ROWS):               row = ""               for j in range(0, NUM_COLS):                    row += str(table[i][j]) + '\t'               out.write(row+'\n')     return################################################################# Reconstructs the LCS and prints it to a file.# Because the sequences can be long, prints the# alignment 50 characters on one line, the other string of 50 characters# on the next line, and then skips one line, as follows:# AATT--GGCTATGCT--C-G-TTACGCA-TTACT-AA-TCCGGTC-AGGC# AAATATGG---TGCTGGCTGCTT---CAGTTA-TGAACTCC---CCAGGC## TATGGGTGCTATGCTCG--T--TACG-CA# TCAT--TGG---TGCTGGCTGCTT--ACA## direction is a 2D table, s1 and s2 are the original DNA# sequences to align and filename is the name of the output file###############################################################def align(direction, s1, s2, filename):     # initialize rows, columns, and newly aligned sequences     row = len(direction) -1     col = len(direction[0]) -1     lcs = ""     # evalutate table for all valid indices     while(row >= 0 and col >= 0):          d = direction[row][col] # start with bottom right          # diagonal, only time add character          if d == "D":               lcs = s1[col] + lcs               row -= 1               col -= 1          # top, update row          elif d == "T":               row -= 1          # left, update column          elif d == "L":               col -= 1          # first, "F"          else:               break     # print the strings to the output file, 50 characters at a time     out = open(filename, 'w')     for i in range(0, len(lcs), 50):          out.write("%s\n" % (lcs[i:i+50]))     out.close()     return### End of functions ######################################################################################### Testing ##########################################################################################if __name__ == "__main__":    ## Calculate LCS score of two sequences    #s = "AGCGTCTA"    #t = "TGCATCTCG"    ## longer test, from lab sheet    #s = "ATGTTGAAGTCAGCCGTTTATTCAATTTTAGCCGCTTCTTTGGTTAATGCAGGTACCATACCCCTCGGAAAGTTATCTGACATTGACAAAATCGGAACTCAAACGGAAATTTTCCCATTTTTGGGTGGTTCTGGGCC"    #t = "ATGTTTTCCCGCAGTCGCTGTGGTTCACTTGTAACAAGTGTGGCTCGCAAAATGTGGAACCACCCAAGCCAGCGCTGGCTCATCTTGATCTGCGTTATATGTTTGCTGTCTTTTGCGCTGGCC"    #s = "AATTGGCTATGCTCGTTACGCATTACTAATCCGGTCAGGCTATGGGTGCTATGCTCGTTACGCA"    #t = "AAATATGGTGCTGGCTGCTTCAGTTATGAACTCCCCAGGCTCATTGGTGCTGGCTGCTTACA"        #s = "TATGCT"    #t = "TGACAGT"        #s = "TGGTAGATTCCCACGAGATCTACCGAGTATGAGTAGGGGGACGTTCGCTCGG"    #t = "GCCTCTAACACACTGCACGAGATCAACCGAGATATGAGTAATACAGCGGTACGGG"        s = convertFileToSequence("yeastPHO12.txt")    t = convertFileToSequence("flyPHO12.txt")    LCS = LCSScore(s, t, "PHO_LCS.txt")    print(s)    print(t)    print("Longest Common Subsequence: " + str(LCS))