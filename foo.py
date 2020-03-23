suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
cardnames = [("Ace", 11),
			("Two", 2),
			("Three", 3),
			("Four", 4),
			("Five", 5),
			("Six", 6),
			("Seven", 7),
			("Eight", 8),
			("Nine", 9),
			("Ten", 10),
			("Jack", 10),
			("Queen", 10),
			("King", 10)]



with open("cards.txt","w") as f:
	cards = "\n".join([f"The {card[0]} of {suite},{card[1]}" for suite in suites for card in cardnames])
	
	f.write(cards)
