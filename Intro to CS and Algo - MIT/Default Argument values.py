def f(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e


f(c=3,a=1,e=5,b=2,d=4)

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

lotsOfParameters2()
lotsOfParameters2(1,2)
lotsOfParameters2(1,c=2)
lotsOfParameters2(1,c=2,3)
lotsOfParameters2(1,e=20,b=3,a=10)

def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

lotsOfParameters3(1, c=2, 3)
lotsOfParameters3(e=5,d=4,c=3,b=2,1)
