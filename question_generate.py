

def quest():
    ques_lis=[]
    filepath = 'questions.txt'
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           #print("Line {}: {}".format(cnt, line.strip()))
           ques_lis.append(str(line.strip()))
           line = fp.readline()
           cnt += 1
    #print(ques_lis)
    return ques_lis
