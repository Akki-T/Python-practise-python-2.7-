def fact(n):
    if (n==0| n==1):
     return 1
    else:
     return n*fact(n-1)


x=int(raw_input("Enter the number : "))
print fact(x)
