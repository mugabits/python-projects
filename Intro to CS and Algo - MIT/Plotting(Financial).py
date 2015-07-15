import pylab


principal = 1000 #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years + 1),values,'ro') #pylab.plot(values,linewidth=30)
pylab.title('5% Growth, Compounded Annually', fontsize=12)
pylab.xlabel('Years of Compounding', fontsize=6)
pylab.ylabel('Value of Principal ($)',fontsize=20)
pylab.show()


#default values are stored in the rc settings in the .rc files (rc=runtime configuration)

#default color for plot is blue
#line style is -
# combined  b -
