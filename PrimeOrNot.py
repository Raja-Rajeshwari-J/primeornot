from tkinter import N


def PrimeOrNot(num):
    flag=0
    if num==0 or num==1:
        print("The given number is not a Prime number")
    elif num==2:
        print("The given number is a Prime number")
    else:
        for div in range(2,(num//2)+1):
            if num%div==0:
                flag=1
    if flag==0:
        print("The given number is a Prime number")
    else:
        print("The given number is not a Prime number")
N=int(input())
PrimeOrNot(N)
