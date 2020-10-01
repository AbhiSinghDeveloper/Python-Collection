x=input()
y=len(x)
z=int(x)
a=z//10
b=z%10
c=0
for i in range(y):
    c+=(b**y)
    b=a%10
    a=a//10
if(c==z):
    print("Armstrong Number")
else:
    print("Not and Armstrong Number")