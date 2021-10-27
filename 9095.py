T=int(input())
num=[ int(input()) for _ in range(T)]
arr = [0,1,2,4,7]
for i in range(5,max(num)+1):
    arr.append(arr[i-3]+arr[i-2]+arr[i-1])
for j in num:
    print(arr[j])