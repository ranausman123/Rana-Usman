Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = int(input("Enter a number: "))
Enter a number: 8
>>> if num < 2:
	print(num, "is not a prime number")
else:
	for i in range(2, num):
		if num % i == 0:
			print(num, "is not a prime number")
			break
		else:
			print(num,"is a prime number")

			
8 is not a prime number
>>> 
