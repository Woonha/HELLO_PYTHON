def factorial(n):
	if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
	print("The value of 5! should be ", 5*4*3*2*1)
	print("The value of 5! is ", factorial(5))
	print("The value of 5! should be 1")
	print("The value of 5! is ", factorial(0))
