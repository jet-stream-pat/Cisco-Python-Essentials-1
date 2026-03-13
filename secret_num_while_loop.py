secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_number = int(input("Enter a number: "))

while user_number != secret_number:
    print("Ha Ha! You are stuck in my loop!")
    user_number = int(input("Enter a number: "))
    
print(secret_number, "Well done! You are free now!")
