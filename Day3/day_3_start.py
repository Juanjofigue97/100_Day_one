print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >=120:
  print ('Can ride')
  age = int(input("What is your age? "))
  if age<= 12:
    print("Pay $5")
  elif age <= 18: 
    print("Pay $7")
  else:
    print("Pay $18")
else:
  print("Can't") 
