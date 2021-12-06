# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Bill = 0
if size == 'S':
    Bill += 15
elif size == 'M':
    Bill += 20
elif size == 'L':
    Bill += 25
else:
    print("Invalid answer")
if add_pepperoni == 'Y' and size == 'S':
    Bill += 2
elif add_pepperoni == 'Y' and (size == 'M' or size == 'L') :
    Bill += 3
if extra_cheese == 'Y':
    Bill += 1

print(f"Your final bill is: ${Bill}.")




