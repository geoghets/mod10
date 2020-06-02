#Does a given number pass the luhn algorithm?
#The luhn algorithm is performed on a number string
#Consider a set of 16 digits, ABCDEFGHJKLMNQRS
# IF (A+B*2+C+D*2+E+F*2+G+H*2+J+K*2+L+M*2+N+Q*2+R+S*2)%0 = 0 , Then it is a luhn passing number
#But wait, it's actually more complicated.
#If 2*X >= 10, The resulting two digits must be added together
# eg. 2*8 = 16, 1+6 = 7

import random

def isMod10(num):                           # type a number, this tells you whether it is Mod10 Passing 
    num = num.replace(" ","")               #removes all spaces
    num = num[::-1]                         #reverses the number.  The last number in the series always gets doubled. To make sure this happens we reverse the series and double the first number
    nums = []                               #the list of numbers is treated as a double initially, but is ultimately treated as a list of individual numbers.  this is that list
    #cycle through
    for i in range(len(num)):               #So now we're going to go through each number and, if it has an even list index, double it
        a = float(num[i])                   #The number we're examining will be called "a"
        if   i%2 != 0 and a<5:              # if a value in nums has an even index and will not exceed 10 if doubled,
            nums = [float(2*a)] + nums        # then double it and add that value to the list
        elif i%2 != 0 and a>=5:             # if the number has an even index and will  exceed 10 if doubled,
            b = str(2*a)                      # then double the value
            c = float(b[0])+float(b[1])       # and then sum the digits of the doubled value
            nums = [c] + nums                 # and append the sum of the digits to the list
        else:                               # If the value does not have an even index
            nums = [a] + nums                 # just append it to the list
    isMod10 = sum(nums)%10 == 0             # And now we have a list of operated-on numbers.  Ad them together to see if they have Modulus 10

    return isMod10

testNum = input("Type in your credit card number")

if isMod10(testNum) == True:
    print("your credit card number is valid")
else:
    print("not a valid number")





