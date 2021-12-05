#Octal to Decimal
octal = input("Enter a string of octal digits: ")
deciVal = 0 
base = 1
  
while octal: 
    digit = int(octal) % 10
    octal = int(octal) / 10
    deciVal += digit * base
    base = base * 8
print("The decimal value is", deciVal)

# One line solution hehe   
# print(int(input('Enter a string of octal digits: '), 8))    

#King Aj Magalona