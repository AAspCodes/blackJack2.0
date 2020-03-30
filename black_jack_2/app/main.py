from .deck import Deck
from .user_input import get_int, get_name
from .player import Player
from .hand import Hand
class Main:
	def __init__(self):

		self.table_min = 10
		number_of_players, number_of_decks = self.get_number_of_players() 
		Deck.ready_deck(number_of_decks)

		# create Dealer
		self.dealer = Player("Dealer")

		# create players
		self.players = self.create_players(number_of_players)
		
		# generate hands
		self.create_initial_player_hands()

		self.create_initial_dealer_hand()

		self.show_states()
	
	def create_initial_dealer_hand(self):
		self.dealer.hands.append(Hand([Deck.draw(),Deck.draw()]))

	def create_initial_player_hands(self):
		for player in self.players:
			bet = self.get_bet(player)
			player.hands.append(Hand([Deck.draw(),Deck.draw()],bet))



	def get_bet(self, player):
		while True:
			try:
				attempted_bet = get_int(self.table_min,player.money,f"{player.name} how much would you like to bet?, {self.table_min} - {player.money}: ")
				bet = player.make_bet(attempted_bet)
			except OutOfMoneyException:
				print("you don't have that much money")
			except Exception:
				print("something went wrong")
				print(Exception.args)
			else:
				return bet

	@staticmethod	
	def create_players(number_of_players):
		players = []
		for _ in range(number_of_players):
			players.append(Player(get_name("What is this player's name: ")))
		# self.show_states()
		# get players money
		for player in players:
			player.money = get_int(100,1_000_000,
			 f"how much money does {player.name} have?\nmin: 100, max: 1 million: ")
		return players

	@staticmethod
	def get_number_of_players():
		message = "Enter the number of players. [1-6]:  "
		number_of_players = get_int(1,6,message)
		number_of_decks = number_of_players * 2
		return number_of_players, number_of_decks

	def show_states(self):
		print(self.dealer)
		for player in self.players:
			print(player)


if __name__ == "__main__":
	Main()
