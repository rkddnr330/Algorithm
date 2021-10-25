def solution(arr):
    sum=0
    for i in arr:
        sum += i
    answer = float(sum/len(arr))
    return answer

#최적화 코드
def solution(arr):
    ans = sum(arr)/len(arr)
    return ans
    #또는
    return sum(arr)/len(arr)