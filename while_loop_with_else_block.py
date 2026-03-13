#when loop finishes early - the else block will run
n = 0 #'n' variable set to 0
while n < 2: #while loops starts and checks if 'n' value is less than 2
    print(n) #if 'n' value is < 2, 'n' value is printed
    n += 1 #increments 1 to the value of 'n' for next iteration of the loop
else: #once 'n' value = 2, else block WILL run as there is no break keyword
    print("Loop finished normally") #message printed

#when loop is stopped with a break - the else block will NOT run
n = 0 #'n' variable set to 0
while n < 2: #while loops starts and checks if 'n' value is less than 2
    print(n) #if 'n' value is < 2, 'n' value is printed
    break #once 'n' value = 2, break is run and the loop is broken
else: #else block WILL NOT as the break keyword is run
    print("Loop finished normally") #message printed
