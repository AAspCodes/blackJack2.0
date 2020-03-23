def get_int(min, max, message):
	
	class TooLowException(Exception):
		pass
	
	class TooHighException(Exception):
		pass

	while True:
		try:
			num = int(input(message))
			if min <= num <= max:
				return num
			elif min > num:
				raise TooLowException()
			elif max < num:
				raise TooHighException()

		except TooLowException:
			print("That value was too low!")
		except TooHighException:
			print("That value was too High!")
		except Exception as e :
			print("That was not a possible input. Try an Integer.")

