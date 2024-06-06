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
print(lines)

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
    print(lines[i])
    for x in lines[i]:
        string = str(lines[i])
        x = str(x)
        word = string.count(x)
        if word > 1:
            repeat.append(x)
    for i in lines[i]:
        if i 


    print(repeat)
    



    
    

