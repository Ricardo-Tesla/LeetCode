def powerOfThree(n):
    if n<=0:
        return False
    while n>1:
        if n%3!=0:
            return False
        n=n//3
    return n==1

n=6
print(powerOfThree(n))