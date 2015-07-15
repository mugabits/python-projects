#import random
#
#def getEven():
#    '''
#    Returns a random even number x, where 0 <= x < 100
#    '''
#    # Your code here
#    even = random.choice(range(0,100,2))
#    #print even
#    return even
#
#def deterministicNumber():
#    return 10
#    
#
#def stochasticNumber():
#    '''
#    Stochastically generates and returns a uniformly distributed even number between 9 and 21
#    '''
#    # Your code here
#    
#    return 2 * random.randint(5, 10)
#    
#
#for i in range(0,10):
#    even = getEven()
#    detmodel = deterministicNumber()
#    stomodel= stochasticNumber()
#    print even, detmodel, stomodel
#    i += 1

#random.random() distribution is uniform over [-1.0,1.0)
#random.randrange() distribution is uniform as well 

#import random
#def dist1():
#    return random.random() * 2 - 1
#
#def dist2():
#    if random.random() > 0.5:
#        return random.random()
#    else:
#        return random.random() - 1 
#
#def dist3():
#    return int(random.random() * 10)
#
#def dist4():
#    return random.randrange(0, 10)
#    
#def dist5():
#    return int(random.random() * 10)
#
#def dist6():
#    return random.randint(0, 10)
#    
#for i in range(0,10):      
#    one = dist1()
#    two = dist2()
#    three = dist3()
#    four = dist4()
#    five = dist5()
#    six = dist6()
#    print one, two, three, four, five, six
    
    
d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1
d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1
d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1
    
print d1,d2,d3