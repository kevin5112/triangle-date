def main():
	a = int(input('enter integer a: '))
	b = int(input('enter integer b: '))
	c = int(input('enter integer c: '))

	# test valid input, receiving false means invalid input
	if not testValidInput(a):
		print("Value of a is not in the range of permitted values.")
		return
	if not testValidInput(b):
		print("Value of b is not in the range of permitted values.")
		return
	if not testValidInput(c):
		print("Value of c is not in the range of permitted values.")
		return

	if not testCondition(a, b, c):
		print("Condition a < b + c fails. Not a Triangle.")
		return
	if not testCondition(b, a, c):
		print("Condition b < a + c fails. Not a Triangle.")
		return
	if not testCondition(c, a, b):
		print("Condition c < a + b fails. Not a Triangle.")
		return

	if checkEquilateral(a, b, c):
		print("Equilateral")
	elif checkIsosceles(a, b, c):
		print("Isosceles")
	else:
		print("Scalene")

	return


def testValidInput(num):
	if num < 1 or num > 200:
		return False
	return True

def testCondition(num1, num2, num3):
	if num1 >= num2 + num3:
		return False
	return True

def checkEquilateral(num1, num2, num3):
	return num1 == num2 == num3

def checkIsosceles(num1, num2, num3):
	if num1 == num2 or num2 == num3 or num1 == num3:
		return True
	return False

if __name__ == "__main__":
	main()