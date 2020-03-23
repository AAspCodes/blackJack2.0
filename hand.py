import textwrap
class Hand:
	def __init__(self, cards=None):
		if cards is None:
			self.cards = []
		else:
			self.cards = cards
		self.bet = 0

	@property
	def value(self):
		return sum([card.value for card in self.cards])

	@property
	def has_busted(self):
		return self.value > 21

	@property
	def has_blackjack(self):
		return self.value == 21

	def add_card(self, card):
		self.cards.append(card)

	@property
	def num_of_cards(self):
		return len(self.cards)

	def split(self):
		if self.can_split:
			return Hand(cards=[self.cards.pop()])
		else:
			raise Exception("can't split",
			 				f"number of cards: {self.num_of_cards}",
			  				f"cards {self.print_cards()}")

	@property
	def can_split(self):
		if not len(self.cards) == 2:
			return False
		elif not self.cards[0] == self.cards[1]:
			return False
		else:
			return True

	def __str__(self):
		return f"{self.print_cards()}, {self.bet}"

	def print_cards(self):
		return f"{[str(card) for card in self.cards]}"
