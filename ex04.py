def DFS(numbers, idx, value, target):
    result = 0
    if idx == len(numbers) :
        if value == target:
            return 1
        else:
            return 0
    result += DFS(numbers, idx+1, value + numbers[idx], target)
    result += DFS(numbers, idx+1, value - numbers[idx], target)
    return result

def solution(numbers, target):
    answer = DFS(numbers, 0, 0 , target)
    return answer