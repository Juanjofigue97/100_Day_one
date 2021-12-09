# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
aux = 0
for i in student_heights:
  sum += i
  aux += 1
Average = sum/aux
print(f"Average: {Average}" )
