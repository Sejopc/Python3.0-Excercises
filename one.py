#one.py

def func():
	print("Func() in one.py")

print("Top Level in one.py")

if __name__ == '__main__':
	print("one.py is being run directly (python one.py)")
else:
	print("one.py has been imported! (import one.py)")