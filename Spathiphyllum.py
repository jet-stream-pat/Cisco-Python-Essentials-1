#this was my attempt at the challenge, which I was able to achieve
#albeit a little messy
big = 'Spathiphyllum'
small = 'spathiphyllum'

plant = str(input())

if plant == big:
    print("Yes - Spathiphyllum is the best plant ever!")
    exit()
elif plant == small:
    print("No, I want a big Spathiphyllum!")
    exit()
else:
    print("Spathiphyllum! Not", plant + "!")
    exit()


#below is the sample code provided
name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")
	
