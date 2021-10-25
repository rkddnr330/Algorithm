def solution(arr1, arr2):
    a=len(arr1)
    b=len(arr1[0])
    ans=[]
    for i in range(a):
        sum=[]
        for k in range(b):
            sum.append(arr1[i][k]+arr2[i][k])
        ans.append(sum)
    return ans