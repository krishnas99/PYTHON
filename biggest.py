x=int(input("enter first number:"))
y=int(input("enter the second number:"))
z=int(input("enter the thired number:"))
if(x>y)and(x>z):
    largest=x
elif(y>x)and(y>z):
    largest=y
else:
    largest=z
print("the largest number is",largest)