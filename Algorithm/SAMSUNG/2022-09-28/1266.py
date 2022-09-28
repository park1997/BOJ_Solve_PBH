from math import factorial

T = int(input())
for test_case in range(1, T + 1):
  skillA, skillB = map(int, input().split())
  probA, probB = 0, 0
  not_prime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
  length = len(not_prime)
  
  # combination 값 미리 구해놓기
  combi = [factorial(18) / (factorial(18-i) * factorial(i)) for i in not_prime]

  for i in range(length):
    probA += combi[i] * (skillA/100) ** not_prime[i] * (1-skillA/100) ** (18-not_prime[i])
    probB += combi[i] * (skillB/100) ** not_prime[i] * (1-skillB/100) ** (18-not_prime[i])
      
  print('#%d %.6f' % (test_case, 1 - probA*probB))