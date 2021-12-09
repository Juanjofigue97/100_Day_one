import random

# Random integer (a,b)
random_integer = random.randint(1,10)
print(f"Random integer: {random_integer}") 

# Random float [0,1)
random_float = random.random()
print(f"Random float: {random_float}")

#Increase range
random_float5 = random_float * 5
print(f"Random float range [0,5): {random_float}")
