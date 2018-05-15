print('Hello World')

def check_even(num):
	list = [number for number in range(0,num) if number % 2 == 0]
	print(list)

check_even(10)