#Decimal To Octal
decimal = int(input("Enter a decimal Integer: "))

if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Octal")   

octalString = " "

while decimal > 0:
    remainder = decimal % 8
    decimal = decimal // 8
    octalString = str(remainder) + octalString
    print('%5d%8d%12s' % (decimal, remainder, octalString))   
print("The octal representation is", octalString)

# err.... ye solution hehe
# decToOct = int(input('Enter a decimal Integer: '))
# print(oct(decToOct).replace('0o', ""))

#===================================================================#

#Octal to Decimal
octal = input("\nEnter a string of octal digits: ")
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
