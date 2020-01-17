

def ans():
    ans_lis=[]
    filepath = 'answers.txt'
    with open(filepath) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           #print("Line {}: {}".format(cnt, line.strip()))
           ans_lis.append(str(line.strip()))
           line = fp.readline()
           cnt += 1
    return ans_lis

