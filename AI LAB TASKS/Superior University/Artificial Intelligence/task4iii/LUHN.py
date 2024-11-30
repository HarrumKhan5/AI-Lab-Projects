def work():
    num=[5,8,9,3,8,0,4,1,1,5,4,5,7,2,8,9]
    x=num.pop(-1)
    print(x)
    print(num)
    num.reverse()
    print(num)
#Doubling even indexes
    for i in range(0, len(num), 2):
        num[i] *= 2
        print(num)
#Subtracting num>9 from 9
    for i in range(len(num)):
        if num[i] > 9:
            num[i] -= 9
            print(num)
    total = sum(num)
    exact=total+x
    print(exact)
    if exact % 10 == 0:
        print("Card num is valid")
    else:
        print("Card num is invalid.")
work()
