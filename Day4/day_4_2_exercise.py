import random

# Split string method
print("Who's Paying")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Generate a random int
number_bill = random.randint(0,len(names)-1) 

print(f"{names[number_bill]} is going to buy the meal today!")
