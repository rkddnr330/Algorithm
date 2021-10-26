n=int(input())
arr=[0,1,2,3]
def f():
    if n==1: return print(arr[1])
    elif n==2: return print(arr[2])
    elif n==3: return print(arr[3])
    else:
        for i in range(4,n+1):
            arr.append(arr[i-2]+arr[i-1])
        return print(arr[n]%10007)
f()