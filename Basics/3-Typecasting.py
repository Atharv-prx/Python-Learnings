#Converting one data type to other

#Explicitly
name = "Yash"
age = 18
gpa = 9
student = True

age = float(age) #age is now float
print(age)
gpa = int(gpa) #gpa is now int
print(gpa)
student = str(student) #student is now string
print(student)

#Implicitly
x = 2
y = 2.5

x = x/y # X got converted into float automatically through operation

print(x)
