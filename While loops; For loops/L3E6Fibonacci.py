def fibonacci (n: int) -> int:
	fib = 0
	fibonacci = [0, 1]
	if n == 0:
		return 0
	elif n == 1:
		return 1
    for i in range(1, 10):
        fib = fibonacci[i] + fibonacci[i-1]
        fibonacci.append(fib)
    return fibonacci


print(fibonacci(7))
