lines = []
N = ''
L = ''
answer = []
while True:
    line = str(input())
    if line:
        lines.append(line)
    else:
        break
#print(lines)

space = 0
for i in lines[0]:
    if i == ' ':
        space += 1
    elif space == 0:
        N += i
    elif space == 1:
        L += i

for i in range(int(N)):
    i += 1
    repeat = []
    #print(lines[i])
    for x in lines[i]:
        string = str(lines[i])
        x = str(x)
        word = string.count(x)
        if word > 1:
            repeat.append(x)
    s = None
    br = 0
    count = 0
    for x in lines[i]:
        if repeat.count(x) > 0:
            if s == 1:
                print('F')
                br = 1
            else:
                s = 1
        else:
            if s == 0:
                print('F')
                br = 1
            else:
                s = 0
        count += 1
        if br == 1:
          break
        if count == int(L):
            print('T')






    

