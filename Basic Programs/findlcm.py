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
 
#Function to return LCM of Two Numbers
# Simple Formulae
# LCM(a, b) = (a x b) / HCF(a, b)

def lcm(a : int,b : int) -> int:
    return (a / hcf(a,b))* b
   
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))  
