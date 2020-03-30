class Player:
	def __init__(self, name):
		self._name = name
		self.hands = []
		self.money = 0

	@property
	def name(self):
		return self._name

	def make_bet(self, bet):
		if bet > self.money:
			raise OutOfMoneyException
		else:
			self.money -= bet
			return bet


	def __str__(self):
		return f"{self.name}, {self.hands}, Money: {self.money}"

	class OutOfMoneyException(Exception):
		pass
