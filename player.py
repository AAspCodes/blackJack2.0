class Player:
	def __init__(self, name):
		self._name = name
		self.hands = []
		self.money = 0

	@property
	def name(self):
		return self._name

	def __str__(self):
		return f"{self.name}, {self.hands}, {self.money}"
