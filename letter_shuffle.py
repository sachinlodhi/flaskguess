import random as ran
import string

def shuffle(word):
    choice =[]
    fin_lis=[]
    #word = 'APOCOLYPSE'
    t=''
    for i in word:
        choice.append(i)

    for i in range(7):
       t=ran.choice(string.ascii_uppercase)
       if t not in word:
           choice.append(t)
       else:
           i-=1
           continue
    ran.shuffle(choice)
    for i in choice:
        if i not in fin_lis:
            fin_lis.append(i)
    fin_lis.remove(' ')
    print(f'Jumbled choicecs are : {fin_lis}')
    return fin_lis