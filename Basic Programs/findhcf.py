#Function to return HCF of Two Numbers

# This function takes two integers a & b and returns a integer
#This function uses recursion for this
def hcf(a : int,b : int) -> int:
   # termination condition 
   # if one number is 0 then other number is HCF of these 2 numbers
    if a == 0:
        return b
   #If first number is not 0 then first number bacomes second%first
    return hcf(b % a, a)
 
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2)) 
