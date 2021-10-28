money = int(input())
def solution(money):
    s = [50000,10000,5000,1000,500,100,50,10,1]
    s_= []
    for i in s:
        k=int(money//i)
        if k >0:
            money -= (k)*i
            s_.append(k)
        else:
            s_.append(0)
    return print(s_)

solution(money)

