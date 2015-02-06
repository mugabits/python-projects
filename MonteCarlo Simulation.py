import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    allsame= 0.0

    for trial in range(numTrials):
        fraction = OneTrial()
        if (fraction == 1.0):
            allsame += 1.0
    print 'counter for same color repetition ' + str(allsame)
    return allsame/numTrials


def OneTrial():
    bucket=[];
    bucket=['Green','Green','Green','Red','Red','Red']
    print str(bucket)
    samecolor = 0
    
    for i in range(3):
        ball = random.randrange(0,len(bucket),1)  
        #index to be deleted from 0 to 6 excluding 6. 
        print str(ball)
        del bucket[ball]
        print str(bucket)
    red = float(bucket.count('Red'))
    green = float(bucket.count('Green'))
    print 'The number of red balls in the bucket is :' + str(red)
    print 'The number of green balls in the bucket is :' + str(green)
    redleft= red/3.0
    print 'red balls left ratio: ' + str(redleft)
    greenleft = green/3.0
    print 'green balls left ratio: ' + str(greenleft)
    
    if (redleft == 1.0):
        samecolor += 1.0
    elif(greenleft == 1.0):
        samecolor += 1.0
    print str(samecolor)
    return samecolor


noReplacementSimulation(100)