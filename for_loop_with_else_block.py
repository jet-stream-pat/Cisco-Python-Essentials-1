#when loop finishes early - the else block will run
for i in range(3): #loop runs through 0-2
    print(i) #value of 'i' is printed as iterates
else: #no break keyword, loop will finish normally and else block WILL run
    print("Loop finished without a break") #message is printed

#when loop is stopped with a break - the else block will NOT run
for i in range(3): #loop runs through 0-2
    print(i) #value of 'i' is printed as iterates
    if i == 1: #if value of 'i' is equal to 1 the program will break
        break #once 'i; value = 1 then break keyword is called into play
else: #because 'break' is called into action, else block will NOT run
    print("The loop in finished without a break") #message is NOT printed
