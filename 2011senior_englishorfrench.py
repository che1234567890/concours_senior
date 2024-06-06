lines = ''
while True:
    line = input()
    if line:
        lines += line
        
    else:
        break

def count(letter, lines):
    number = 0
    for i in lines:
        if i == letter:
            number += 1 
        elif i == letter.upper():
            number += 1
        else:
            pass
    return number

print(count('s', lines))
print(count('t', lines))
if count('s', lines) >= count('t', lines):
    print('French')
else:
    print('English')

