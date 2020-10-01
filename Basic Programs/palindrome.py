x=input()
y=len(x)
z=int(x)
a=z//10
b=z%10
c=0
for i in range(y,0,-1):
    c+=b*(10**(i-1))
    b=a%10
    a=a//10
if (c==z):
    print("Palindrome")
else:
    print("Not a Palindrome")