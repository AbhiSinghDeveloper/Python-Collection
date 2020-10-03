#This is a program to reverse the digits.
#Example:
#Input- 12345
#Output=54321


def reverseFunction(digit):
   reversedDigit=0
   while(digit>0):
     remainder=digit%10
     reversedDigit=(10*reversedDigit)+remainder
     digit=digit//10
   return reversedDigit


digit=int(input("Enter your digit to be reversed : "))
reversed=reverseFunction(digit)
print("The reversed digit is: ",reversed)
