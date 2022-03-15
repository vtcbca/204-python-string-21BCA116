n=input("Enter any sentence:")
if(n==n[::-1]):
    print("The string is pelindrome")
else:
    print("The string is not a pelindrome")
l=n.split()
for i in l:
    print(i)
