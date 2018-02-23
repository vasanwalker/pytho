m=int(input("Enter number: "))
rev=0
while(m>0):
    dig=m%10
    rev=rev*10+dig
    m=m//10
print("Reverse of the number:",rev)
