def countPossible(left2, left, mid, right, right2):
      global nums
      find_max = max(nums[left2], nums[left], nums[right], nums[right2])
      if find_max < nums[mid]:
            return nums[mid] - find_max
      else:
            return 0
#import sys
#sys.stdin = open("input.txt", "r")
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
      result = 0
      N = int(input())
      nums = list(map(int, input().split()))
      for s in range(2, N-2, 1):
            result += countPossible(s-2, s-1, s, s+1, s+2)
      
      print("#{} {}".format(test_case, result))