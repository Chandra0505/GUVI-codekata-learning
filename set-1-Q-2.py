n = int(input("Enter your number"))
if n < 0:
	print("Invalid number")
else:
	if n % 2 == 0:
		print("Even")
	else:
		print("Odd")