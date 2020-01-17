
def transform(que,ans,usr):
    t_que =[i for i in que]
    t_ans = [i for i in ans]
    print(f't_que {t_que}')
    #print(f't_que {t_ans}')
    for i,j,k in zip(t_que,t_ans,range(len(t_ans))):
        if i == '_':
            if j == usr:
                t_que[k] = j

    ans=''
    for i in t_que:
        ans+=i
    #print( ans)
    return ans


