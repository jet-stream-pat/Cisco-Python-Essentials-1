#quiz q1
#correct
for i in range(0, 11):
    if i == (1):
        print(i)
    elif i == (3):
        print(i)
    elif i == (5):
        print(i)
    elif i == (7):
        print(i)
    elif i == (9):
        print(i)
    elif i == (11):
        print(i)

#quiz q2
#correct
x = 1
while x < 11:
    print(x)
    x += 1

#quiz q3
#correct
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    if ch != "@":
        print(ch, end="")

#quiz q4
#correct - no continue statement but this is more readable and cleaner
for digit in "0165031806510":
    if digit == "0":
        digit = ('x')
    print(digit, end="")


#quiz q5
#predict the outcome
#4 3 2 0
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

#quiz6
#predict the outcome
#
for i in range(0, 6, 3):
    print(i)
 
            
    


    
