def factorial(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

if __name__ == '__main__':
	print("The value of 5! should be ", 5*4*3*2*1)
	print("The value of 5! is ", factorial(5))
	print("The value of 0! should be 1")
	print("The value of 0! is ", factorial(0))
