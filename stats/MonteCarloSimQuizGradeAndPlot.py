import random
def sampleQuizzes():
    yes = 0
    for e in range(10000):
        mid1 = random.choice(range(50, 80))
        mid2 = random.choice(range(60, 90))
        finalExam = random.randrange(55, 95)
        score = mid1*0.25 + mid2*0.25 + finalExam*0.5
        if score >= 70 and score <= 75:
            yes += 1
        return yes / 10000.0
print sampleQuizzes()



import pylab
def plotQuizzes():
    pylab.hist(generateScores(10000), bins=7)
    pylab.title("Distribution of scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.show()
plotQuizzes()