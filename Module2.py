#instructions
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")

print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

#using newline characters
#\n - escape character#
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

print("My\nname\nis\nBond.", end=" ")
print("James Bond.")

#using multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

#using positional arguments
print("My name is", "Python.")
print("Monty Python.")

#using keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.")

#end= #used to pass arguments into the console
print("Hello World!","My name is", end=" ")
print("Patrick.")

print("My name is ", end="")
print("Monty Python.")

#sep= #separates arguments printed to console
print("My", "name", "is", "Monty", "Python.", sep="-")
print("Hello","my","name","is","Patrick.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#using both keyword arguments
#sep=
#end=
print("Programming","Essentials","in", sep="***" ,end="...")
print("Python")
#the above code will print 'Programming***Essentials***in...Python' to the console

#two examples of literals below that both produce the same outcome when printed to the console
print("2") #string literal
print(2) #numeric literal

#numeric literal formats
print(11111111) #the numeric value can simply be display with a string of numbers
print(11_111_111) #the number can be separated by underscores _
print(-11111111) #the same applies to negative/minus numeric values, just include the minus sign
print(-11_111_111)

#octal numbers - if a numeric value is prefixed with 0o (zero-o) then its treated as an octal number
print(0o23) #0o23 is equal to 83, and 83 will print to the console

#hexadecimal numbers - if a numeric value is prefixed with 0x (zero-x) then its treated as a hexidecimal number
print(0x123) #0x123 is equal to 291, and will print 291 to the console

#float / floating-point numbers
print(0.4) #will print 0.4 to the console
print(.4) #will again print 0.4 to the console

#using e (exponent) to calculate scientific notation
print(3E8) # will return 300000000.0 to the console (3 x 10 power 8)

#encoding a quote inside a string
#the following quoted code would generate an error message print("I like "Monty Python.")
#two alternatives to get around this
print("I like\"Monty Python\"") #option 1 is to use the escape character \ (backslash)
print('I like "Monty Python"') #option 2 is to bookend the quote with apostrophes

#embedding an apostrophe into a string already placed between apostrophes
print('I\'m Patrick') #option 1 - using the escape backslash character (\)
print("I'm Patrick.") #option 2 - bookend with quotation marks

#Boolean values (true/false)
print(1>0) #prints true because 1 is greater than 0
print(1<0) #prints false because 0 is less than 1

#challenge
#produce code across three lines to print the following
#"I'm"
#""learning""
#"""Python"""
print('"I\'m"')
print('""learning""')
print('"""Python"""')
#the above code is correct :)
























