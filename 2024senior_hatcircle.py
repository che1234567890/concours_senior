lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

overall = 0
nm_lines = int(lines[0])/2
for i in range(int(nm_lines)):
    a = int(i + 1)
    u = int(nm_lines + 1 + i)
    e = lines[a]
    f = lines[u]
    if  e == f:
        overall += 1    

        

print(overall)

