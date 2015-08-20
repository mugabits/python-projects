import string
import sys

pathToTxt = '/Users/jmugz3/Github/PythonTraining/words.txt'
pathToCsv = '/Users/jmugz3/Github/PythonTraining/words.csv'
e = sys.exc_info()[:]

def loadtext(path):
    
    try:
        readTxt = open (path, 'r',0)
        row = readTxt.readline()
        rowitems = string.split(row)
        #print type(rowitems)
        #print type(row)
     
    except:
        print 'There was an error loading your file'
        print e
    
    print row == rowitems
    readTxt.close()
    
    try:   
        word = raw_input('Enter a word to search in the list:')
        print word 
        for item in rowitems:
            print word
            if (item == word):
                print word + ' exists in the list'
                break
            elif (item != word):
                print word + ' does not exist in the list' 
                list2 = AddWord(word, rowitems)
                print list2[-1] + ' was added to the list' 
                return list2
            else:
               print 'It seems like you did not type a word'          
    except:
        print 'You entered an invalid word'
        print e
            
def AddWord(w,wlist):
    #print wlist
    wlist.append(w)
    return wlist
    
loadtext(pathToTxt)