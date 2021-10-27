num=[i for i in range(1,10001)]
for i in range(1,10001):
    length=len(str(i))
    mob=i
    for l in range(length):
        mob+=int(str(i)[l])
    if mob in num: num.remove(mob)
for i in range(len(num)): print(num[i])