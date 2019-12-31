import random as ran

def generator():
    file=open('sowpods.txt','r')
    lis=[line.rstrip('\n') for line in file] #copying all the words of the file into a list
    length=len(lis)
    guess=ran.randrange(length)  #guessing the word between 0 and length of the lilst
    #print('Current Guess is : {}'.format(lis[guess]))#printing the guesse index
    word=str(lis[guess])
    return word
