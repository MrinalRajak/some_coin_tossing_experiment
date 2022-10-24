'''
# 1:write python code to simulate single fair coin tossing experiment
# to numerically verify the probability of appearance of Heads and Tails.

import numpy as np
import matplotlib.pyplot as plt
from random import randint

heads= 0
tails= 0

flip= int(input("How many coin tosses are you going to do?:"))

for i in range(flip):
    result= randint(0,1)
    if result == 0:
        #print "Heads"
        heads +=1
    else:
        #print "Tails"
        tails +=1

print ("The results are:")
print ("Heads:", heads)
print ("Tails:", tails)

print ("Probability of heads:", heads/float(flip))
print ("Probability of tails:", tails/float(flip))


# 2:simulate the tossing of two fair coins a million times
# and count the no.of times you get double Head and hence
# compute probability of appearance of double Heads is (1/4).

import numpy as np
import matplotlib.pyplot as plt
from random import randint

double_heads=0

flip = int(input("How many coin tosses are you going to do?:"))

for i in range(flip):         #Take flip= 1000000
    result1= randint(0,1)
    result2= randint(0,1)
    results=[result1,result2]
    #print results
    if result1==result2==1:
        double_heads +=1

print ("No.of double heads:", double_heads)
print ("Probability of double heads", (double_heads)/float(flip))

while (((double_heads)/float(flip))<=0.26):
    print ("probability of getting double heads is (1/4).")
    break



# 3:write python code to simulate single biased  coin tossing experiment
# to numerically verify the probability of appearance of Heads and Tails.

import numpy as np
import matplotlib.pyplot as plt
from random import randint

Trails= 100
biased= 0.8
experiments= 50

def event(n,biased,size):
    outcome= np.random.binomial(n,biased,size)
    return outcome


outcome= event(Trails,biased,experiments)

print ("No.of heads in each experiment:\n", outcome)
print ("No.of tails in each experiment:\n", Trails-outcome)

Prob_heads= np.sum(outcome)/float(experiments)
Prob_tails= np.sum(Trails-outcome)/float(experiments)

print ("Probability of getting heads:", Prob_heads)
print ("Probability of getting tails:", Prob_tails)



# 4:simulate single rolling a dice a million times and determine the 
# probability of getting 3 or 6 on top face.(Answer should also be verified
# analitically)

import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint

Count= 0

Roll=int(input("How many rolls of dice do you want?:"))

for i in range(Roll):
    outcome= random.randint(1,6)
    #print outcome
    if outcome ==3:
        Count +=1
    if outcome ==6:
        Count +=1

print ("No.of times we get 3 or 6:", Count)
print ("Probability of getting 3 or 6:", Count/float(Roll))



# 5:write python code to simulate rolling two dices a million times
# and determine the probability of appearance of same face in
# two successive throws.(Answer should be verified Analytically)


import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint

Count= 0

Roll= int(input("How many rolls of dice do you want?:"))

for i in range(Roll):               #Take Roll= 1000000
    outcome1= random.randint(1,6)
    outcome2= random.randint(1,6)
    outcome= [outcome1,outcome2]
    print (outcome)
    if outcome1 == outcome2:
        Count += 1

print ("No.of times we get same outcome:", Count)
print ("Probability of getting same outcome:", Count/float(Roll))



# 6:Find the probability distribution P(n) for throwing a Sum 'n'
# with two dices. plot P(n) as a function of 'n' .
# [ Answer should be first analytically calculated and then
# numerically verified].


import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint

n=1000000
x=np.random.choice([1,2,3,4,5,6],(n,2))
sum_arr=np.sum(x,axis=1)
probsum=np.bincount(sum_arr,minlength=13)/float(n)
print ("\nTheoretical probability of getting a sum from 2 to 12 are: ",0.028,0.056,0.083,0.111,0.138,0.111,0.083,0.056,0.028)
print ("Simulated probability of getting a sum from 2 to 12 are: ",probsum[2:])
plt.bar(range(2,13),probsum[2:])
plt.xlabel('n')
plt.xticks()
plt.ylabel('$P(n)$')
plt.yticks()
plt.title('Probability distribution of sum with two dice.')
plt.show()



# 7: Repeat computer simulation of question no.6 ,for simultaneous rolling
# 3,5 and 10 dices and plot the respective P(n) as a function of 'n'.


import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint


n=1000000
s=10 # no.of die
x=np.random.choice([1,2,3,4,5,6],(n,10))
sum_arr=np.sum(x,axis=1)
probsum=np.bincount(sum_arr,minlength=6*s+1)/float(n)
plt.bar(range(s,6*s+1),probsum[s:])
plt.xlabel('n')
plt.xticks()
plt.ylabel('$P(n)$')
plt.yticks()
plt.title('Probability distribution of sum with {0:02} dice '.format(s))
plt.show()
                                                


# 8:Find the probability of having 2 heads out of 10 coins tossed.
# (Answer should be first analitically calculated and then numerically
# verified).


import numpy as np
import math
import random
import matplotlib.pyplot as plt
from random import randint


def test():
    number_heads= 0
    for flip in range(10):
        number_heads += random.randint(0,1)
    return (number_heads >= 2)


def experiment(n):
    successes= 0
    for t in range(n):
        successes += int(test())
    print (successes)
    print (n)
    print (successes/float(n))

experiment(100000)

def theoretical():
    successes = 0
    for k in range (11):
        successes += (math.factorial(10)/(math.factorial(2)*math.factorial(10-2)))*(0.5)**2*(0.5)**8
    possible_results = 10
    return successes/float(possible_results)

print (theoretical())



# 9:Flip a coin n-times and show how the fractions of Head and Tail vary
# with number of trials.[can plot difference (between Head and Tail)fractions
# to number of trials.]

import numpy as np
import matplotlib.pyplot as plt
from random import randint
n=100000
N= range(1,n)

x=np.random.choice([0,1],size = n)
y= [np.sum(x[:i])/float(i) for i in N]
z= [np.sum(x[:i]==0)/float(i) for i in N]

#print y
#print z
plt.plot(N,z)    
plt.plot(N,y)
plt.show()
'''

