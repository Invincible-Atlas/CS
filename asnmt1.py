# ask for name
name = input("What's your name? ")
print(f"Hi, {name}")
# ask for age
age = input("How old are you? ")
# print age+1
print(f"Next year you will be {str(int(age)+1)} years old")
# Ask for amount of flour
flourAmt = input("How much flower? ")
# print flouramt*2
print(f"You need this much flower: {str(float(flourAmt)*2)}")
# ask for both joke parts
jp1 = input("Joke part 1")
jp2 = input("Joke part 2")
# print them
print(f"{jp1}\n{jp2}")
# Ask for personal info
color = input("Fav color? ")
num = input("Fav number? ")
# This aint JS, I can redeclare variables whenever I want and you can't stop me
name = input("Best friend's name? ")
print(f"{name} thinks there are only {num} shades of {color}")