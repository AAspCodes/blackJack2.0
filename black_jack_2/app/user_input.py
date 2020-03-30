def get_int(min, max, message):
	
	class TooLowException(Exception):
		pass
	
	class TooHighException(Exception):
		pass

	while True:
		try:
			num = int(input(message))
				
			if min > num:
				raise TooLowException
			elif max < num:
				raise TooHighException

		except TooLowException:
			print("That value was too low!")
		except TooHighException:
			print("That value was too High!")
		except Exception as e :
			print("That was not a possible input. Try an Integer.")

		else:
			return num


def get_name(message):

	class NonAlphanumericException(Exception):
		pass

	while True:
		try:
			name = input(message)
			if not name.isalpha():
				raise NonAlphanumericException

		except NonAlphanumericException:
			print("Only letters please!")
		
		except Exception as e:
			print("woh, Learn something new!!")
			print("That's not a name, try again.")
			print(e.args, e)
		else:
			return name.capitalize()
