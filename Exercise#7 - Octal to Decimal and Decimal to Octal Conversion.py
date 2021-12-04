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
    print("%5d%8d%12s" % (decimal, remainder, octalString))   
print("The octal representation is", octalString)
#===================================================================#

#Octal to Decimal
octal = input("\nEnter a string of octal digits: ")
decimalV = 0
length = len(octal)
for n in octal:
    length -= 1
    decimalV += pow(8, length) * int(n)
print("The integer value is", decimalV)

# Or a better way   
# print("Better way", int(octal, 8))    

#King Aj Magalona