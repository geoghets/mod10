import random

def isMod10(num):
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

#brute force mod10 generator (just guesses 16 digit numbers until it finds one that works) #makes a list of mod10 passing numbers
def generateMod10(num):
    mod10list = []

    while len(mod10list) < num:                                     # Choose how many mod10 numbers you want it to create
        r = random.randint(4000000000000000, 4999999999999999)    #You can use any range of numbers you want.  All Visa Card numbers are between 4000000000000000 and 4999999999999999)
        r = str(r)                                                # So you have a random 16 digit number, now turn it into a string, and run it through the MOD10 checker
        if isMod10(r) == True:
            mod10list.append(r)
    
    a = [mod10list[i] for i in range(len(mod10list))]    
    return a
    
print(generateMod10(8))
