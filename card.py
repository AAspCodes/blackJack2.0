import textwrap
class Card:
	def __init__(self, name, value):
		self._name = name
		self._value = value

	@property
	def name(self):
		return self._name

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		if self.value == 11 and value == 1:
			self._value = value
		else:
			raise Exception(textwrap.dedent(f"""\
								you can only change the value of a high ace,
								you tried to change the value of '{self.name}'
								that has a value of '{self.value}'"""))