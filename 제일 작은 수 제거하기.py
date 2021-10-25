def solution(arr):
    min = arr[0]
    if arr == [10]: arr = [-1]
    else:
        for i in range(1,len(arr)):
            if min > arr[i]:
                min = arr[i]
        arr.remove(min)
    return arr

#min 그냥 써도 됨!
def solution(arr):
    if arr == [10]: arr = [-1]
    else:
        arr.remove(min(arr))
    return arr
#리스트에서 min 써도 저절로 최소값 찾아줌