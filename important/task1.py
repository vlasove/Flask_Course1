import requests
A = float(input())
B = float(input())
C = float(input())

if A == 0 :
    #BX + C = 0
    if B == 0:
        print("корней нет")
    else:
        print("один корень")
else:
    D = B**2 - 4*A*C
    if D > 0:
        print("два корня")
    elif D == 0:
        print("один корень")
    else:
        print("корней нет")