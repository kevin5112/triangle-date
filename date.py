def main():
	month = int(input("enter a month: "))
	day = int(input("enter a day: "))
	year = int(input("enter a year: "))

	if not checkValidMonth(month):
		print("Value of month not in the range 1...12.")
		return

	if not checkValidDay(day):
		print("Value of month not in the range 1...31.")
		return

	if not checkValidYear(year):
		print("Value of month not in the range 1812...2012.")
		return	

	NextDate(month, day, year)
	return

def NextDate(month, day, year):

	if not checkValidDate(month, day, year):
		return

	if checkLeapYear(year):
		if month == 2 and day == 29:
			day = 1 
			month = 3
		elif checkMonthsWith30Days(month) and day == 30:
			day = 1
			monthAndYearTuple = checkEndoftheYear(month, year)
			month = monthAndYearTuple[0]
			year = monthAndYearTuple[1]
		elif day == 31:
			day = 1
			monthAndYearTuple = checkEndoftheYear(month, year)
			month = monthAndYearTuple[0]
			year = monthAndYearTuple[1]
		else:
			day += 1
	else:
		if month == 2 and day == 28:
			day = 1
			month = 3
		elif checkMonthsWith30Days(month) and day == 30:
			day = 1
			monthAndYearTuple = checkEndoftheYear(month, year)
			month = monthAndYearTuple[0]
			year = monthAndYearTuple[1]
		elif day == 31:
			day = 1
			monthAndYearTuple = checkEndoftheYear(month, year)
			month = monthAndYearTuple[0]
			year = monthAndYearTuple[1]
		else:
			day += 1


	print("Next date is: {}-{}-{}".format(month, day, year))
	return


def checkEndoftheYear(month, year):
	if month == 12:
		month = 1
		year += 1
	else:
		month += 1

	return (month, year)

def checkValidDate(month, day, year):
	if not checkDaysinMonth(month, day):
		print("Invalid Input Date.")
		return False

	if checkLeapYear(year):
		if month == 2 and day > 29:
			return False

	elif not checkValidFeb(month, day):
		return False
	return True

def checkValidFeb(month, day):
	if month == 2 and day > 28:
		return False
	return True

def checkLeapYear(year):
	if year % 100 != 0:
		if year % 4 == 0:
			return True
	else: 
		if year % 400 == 0:
			return True
	return False

def checkDaysinMonth(month, day):
	if checkMonthsWith30Days(month) and day > 30:
		return False
	return True

def checkMonthsWith30Days(month):
	if (month <= 7 and month % 2 == 0) and (month > 7 and month % 2 == 1):
		return True
	return False

def checkValidMonth(month):
	if month < 1 or month > 12:
		return False
	return True

def checkValidDay(day):
	if day < 1 or day > 31:
		return False
	return True

def checkValidYear(year):
	if year < 1812 or year > 2012:
		return False
	return True

if __name__ == "__main__":
	main()