def get_int(min, max, message):
	while True:
		try:
			num = int(input(message))
			if min <= num <= max:
				return num
			else:
				raise Exception
		except Exception as e :
			print("that was not a possible input.")
