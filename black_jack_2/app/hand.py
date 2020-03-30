import textwrap
class Hand:
	def __init__(self, cards=None, bet=0):
		if cards is None:
			self.cards = []
		else:
			self.cards = cards
		self.bet = bet

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
			  				f"cards {self.cards_to_string()}")

	@property
	def can_split(self):
		if not len(self.cards) == 2:
			return False
		elif not self.cards[0] == self.cards[1]:
			return False
		else:
			return True

	# def __str__(self):
	# 	return f"Hand:{self.cards_to_string()}, {self.bet}"

	def __repr__(self):
		return f"Hand:{self.cards_to_string()}, Bet:{self.bet}"

	def cards_to_string(self):
		return f"{[str(card) for card in self.cards]}"
