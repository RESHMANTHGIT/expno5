def Fibonacci(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

x = int(input())
lst = []
for i in range(1,x+1):
    fib = Fibonacci(i)
    lst.append(fib)
print(lst)
