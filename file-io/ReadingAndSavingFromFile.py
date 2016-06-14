#import string 
import pylab
import numpy as np

path ='temps.txt'

def BostonTemp():
    inFile = open(path,'r')
    line = inFile.readline()
    LowTemp = []
    HighTemp = []
   
    #print line
    #for line in inFile:
    #    print line,
        
    for line in inFile:
        fields = line.split() #or string.split(line)
        if len(fields) != 3 or 'Boston'== fields[0] or 'Day' == fields[0]:
            continue
        else:
            LowTemp.append(int(fields[1]))
            HighTemp.append(int(fields[2]))
    return (LowTemp,HighTemp)

def producePlot(low, high):   
   for i in range(1,32):
    diffTemps=list(np.array(high)-np.array(low))
    print diffTemps
    pylab.figure(1)
    pylab.plot(range(1,32),diffTemps)
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.show()
    
(lowT,highT) = BostonTemp()
producePlot(lowT,highT)
