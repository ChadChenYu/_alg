##請用四種方法算 f(n) = 2**n (2的 n 次方）
## way 1:
def power2n(n):
    return 2 ** n
  ## 複雜度O(1)

## way 2:
def power2n(n):
    if n == 0:
        return 1
    return power2n(n-1) + power2n(n-1)
  ## 複雜度O(2^n)

## way 3:
memo = {0: 1}

def power2n(n):
    if n in memo:
        return memo[n]
    memo[n] = power2n(n-1) + power2n(n-1)
    return memo[n]
  ## 複雜度O(n)

## way 4:
def power2n(n):
    if n == 0:
        return 1
    return 2 * power2n(n-1)
  ## 複雜度O(n)

## 使用CHATGPT協助完成，連結https://chatgpt.com/share/68c8db00-6790-8009-9ffd-45065ff54c80
