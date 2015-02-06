import string
import sys

e = sys.exc_info()[:]

#Edit the path before running the code
path = '/Users/jmugz3/Github/PythonTraining/words.txt'
path2 = 'notme.txt'
path3 = '/Users/jmugz3/Github/PythonTraining/words2.txt'

def loadWords(p):
	readTxt = open(p, 'r', 0)
	line = readTxt.readline()
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

loadWords(path)

# Uncomment the following function if you want to try the code template

def loadWords2(p):
    try:
        readTxt = open(p, 'r', 0)
 	#line of code to be added here#
        
        lineItems = readTxt.readline()
        wordlist = string.split(lineItems)
        print "  ", len(wordlist), "words loaded."
        return wordlist
    except: 
        #print e
        print "The wordlist doesn't exist; using some fruits for now"
        fruits = ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
        print fruits
        return fruits

loadWords2(path2)