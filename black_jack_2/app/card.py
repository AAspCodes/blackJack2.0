import textwrap

class Card:
	def __init__(self, name, card_type, value):
		self._name = name
		self._card_type = card_type
		self._value = value
		
	@property
	def name(self):
		return self._name

	@property
	def card_type(self):
		return self._card_type

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		

		if self.value == 11 and value == 1:
			self._value = value
		else:
			raise CantSetValueException(textwrap.dedent(f"""\
								you can only change the value of a high ace,
								you tried to change the value of '{self.name}'
								that has a value of '{self.value}'"""))
	
	def __str__(self):
		return f"{self.name}, {self.card_type}, {self.value}"

	def __eq__(self, other_card):
		
		return (self.card_type == other_card.card_type and
			 	self.value == other_card.value)


class CantSetValueException(Exception):
		pass
