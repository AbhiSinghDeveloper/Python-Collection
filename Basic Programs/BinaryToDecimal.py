def binary_to_decimal(binary): 
    decimal = 0 
    binary = list(str(binary)) #convert binary to a list 
    binary = binary[::-1]      #reverse the list 
    power = 0   #declare power variable (for 1st elem == 0) 
    for number in binary: 
        if number == '1': 
            decimal += 2**power     
        power += 1 #increase power by 1    
    return decimal 

print(binary_to_decimal(100010100010))