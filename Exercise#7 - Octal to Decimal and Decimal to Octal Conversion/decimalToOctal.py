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
#King Aj Magalona 
