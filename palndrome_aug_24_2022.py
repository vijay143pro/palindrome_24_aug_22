def nav(n):
    if(n==n[::-1]):
        return 1

    
n=input("Enter text/number to check palindrome or not")
res=nav(n)
if(res):
    print("it is a palindrom",n)
else:
    print("not a palindrom",n)


