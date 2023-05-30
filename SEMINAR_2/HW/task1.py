n = int(input())
zero = 0
one = 0
for i in range(n):
    a = int(input())
    if a == 0:
        zero += 1
    else:
        one +=1
        if zero > one:
            print("zero")
        else:
            print("one")
