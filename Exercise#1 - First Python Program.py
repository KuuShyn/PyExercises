#King Aj Magalona
#v1.2
#Second Attempt hehehe forgot age = "int"(input)...
userName = (input("Enter username: "))
age = int(input("Enter your age: "))
firstNumber = int(input("Enter the first number: ")) 
secondNumber = int(input("Enter the Second Number: "))


# while True:
#   try:
#     age = int(input("Enter your age: "))   
#   except ValueError:
#     print("Numbers Bruh like 1 2 3 4 5.. (>.>)")  
#     continue    
#   else:  
#     if age > 0:        
#       break
#     print("Invalid age entered")  

# while True:
#   try:
#     firstNumber = int(input("Enter the first number: "))  
#   except ValueError:
#     print("Numbers Bruh like 1 2 3 4 5.. (>.>)")  
#     continue
#   else:
#       break

# while True:
#   try:
#     secondNumber = int(input("Enter the Second Number: "))
#   except ValueError:
#     print("That is not a valid number")  
#     continue
#   else:
#       break

print("The username is", userName, "and the age is", age)
print("The product is", firstNumber * secondNumber)

