def add(a, b): 
 return a + b 
def subtract(a, b): 
 return a - b
def multiply(a, b):
 return a * b
def divide(a, b):
 return a / b
print("select an operation -\n" 
"1. Add\n" 
"2. Subtract\n" 
"3. Multiply\n"
"4. Divide\n") 
c = int(input("Select operations form 1, 2, 3, 4 :")) 
num_1 = int(input("Enter a: ")) 
num_2 = int(input("Enter b: "))
if c == 1: 
 print(num_1, "+", num_2, "=", add(num_1, num_2)) 
elif c == 2:
 print(num_1, "-", num_2, "=", subtract(num_1, num_2)) 
elif c == 3:
 print(num_1, "*", num_2, "=", multiply(num_1, num_2)) 
elif c == 4:
 print(num_1, "/", num_2, "=", divide(num_1, num_2)) 
else:
 print("Invalid Input!")






