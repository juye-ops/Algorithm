def solution(n, times):
    left = 0
    right = n*max(times)
    while left<=right:
        mid = (left+right) // 2
        total = sum(map(lambda x: mid//x, times))
        if total >= n:
            right = mid - 1
            answer=mid
        else:
            left = mid + 1
    return answer