n=int(input())
arr=[0,1,3]
for i in range(3,n+1):
    arr.append(arr[i-1]+2*arr[i-2])
print(arr[-1]%10007)