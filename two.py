import one

print("Top Level in two.py")

one.func()

if __name__ == '__main__':
	print("two.py is being run directly (python two.py)")
else:
	print("two.py has been imported (import two.py)")