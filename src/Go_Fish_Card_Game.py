import random
from collections import deque


# Stack class to represent the deck of cards
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # Add a card to the stack (deck)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None  # Remove and return top card if stack isn't empty

    def is_empty(self):
        return len(self.stack) == 0  # Check if the deck is empty

    def size(self):
        return len(self.stack)  # Return number of cards in the deck


# Player class to represent each player's state and behavior
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = deque()   # Cards in hand
        self.books = []       # Completed books (4 of the same rank)

    def draw_card(self, deck):
        if not deck.is_empty():  # Draw a card from the deck if it's not empty
            card = deck.pop().upper()
            self.hand.append(card)
            print(f"{self.name} drew a card.")

    def ask_for_rank(self):
        # If the hand is empty, no rank can be asked
        if not self.hand:
            return None

        # Show player's hand and prompt for a rank
        print(f"{self.name}'s hand: {', '.join(self.hand)}")
        while True:
            rank = input(f"{self.name}, enter the rank you want to ask for: ").strip().upper()
            if rank in (card.upper() for card in self.hand):  # Check if the rank is in hand (case-insensitive)
                return rank
            else:
                print("Invalid rank. Please choose a rank that you have in your hand.")

    def give_cards(self, rank):
        # Give all cards of the requested rank (case-insensitive)
        rank = rank.upper()
        cards = [card for card in self.hand if card.upper() == rank]
        self.hand = deque([card for card in self.hand if card.upper() != rank])
        return cards

    def receive_cards(self, cards):
        # Add received cards to hand and check for books
        for card in cards:
            self.hand.append(card)
        self.check_books()

    def check_books(self):
        # Count frequency of each rank (case-insensitive)
        ranks = {}
        for card in self.hand:
            key = card.upper()
            ranks[key] = ranks.get(key, 0) + 1

        # Check for 4-of-a-kind (a book)
        for rank, count in ranks.items():
            if count == 4:
                self.books.append(rank)
                self.hand = deque([card for card in self.hand if card.upper() != rank])
                print(f"{self.name} collected a book of {rank}s!")

    def hand_size(self):
        return len(self.hand)  # Number of cards in hand

    def __str__(self):
        return f"{self.name} - Books: {len(self.books)}"  # String representation for player summary


# Initialize and shuffle a new deck
def initialize_deck():
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 2-10, J, Q, K, A
    deck = Stack()
    cards = [rank.upper() for rank in ranks] * 4  # 4 of each rank
    random.shuffle(cards)  # Shuffle the deck
    for card in cards:
        deck.push(card)
    return deck


# Main game logic
def play_game(num_players=2, cards_per_player=5):
    deck = initialize_deck()
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    # Deal cards to each player
    for _ in range(cards_per_player):
        for player in players:
            player.draw_card(deck)

    turn = 0
    while not deck.is_empty():
        current_player = players[turn % num_players]
        opponent = players[(turn + 1) % num_players]
        print(f"\n{current_player.name}'s turn:")

        # If player has no cards, draw one
        if current_player.hand_size() == 0:
            current_player.draw_card(deck)
            turn += 1
            continue

        # Player chooses a rank to ask for
        rank = current_player.ask_for_rank()
        if not rank:
            current_player.draw_card(deck)
            turn += 1
            continue

        print(f"{current_player.name} asks: Do you have any {rank}s?")
        cards = opponent.give_cards(rank)

        if cards:
            # If opponent has the cards, give them to current player
            print(f"{opponent.name} gives {len(cards)} {rank}(s) to {current_player.name}.")
            current_player.receive_cards(cards)
        else:
            # If opponent doesn't have the cards, "Go Fish"
            print(f"{opponent.name} says: Go Fish!")
            current_player.draw_card(deck)

        current_player.check_books()
        turn += 1

    # Game ends when deck is empty
    print("\nGame Over!")
    for player in players:
        print(player)

    # Determine the winner(s)
    max_books = max(len(p.books) for p in players)
    winners = [p for p in players if len(p.books) == max_books]

    if len(winners) == 1:
        print(f"\nWinner: {winners[0].name} with {max_books} books!")
    else:
        print("\nIt's a tie between: " + ", ".join(p.name for p in winners))


# Entry point for the game
if __name__ == "__main__":
    try:
        # Get number of players and cards per player from user
        num_players = int(input("Enter number of players (2–6): "))
        cards_per_player = int(input("Enter number of cards per player: "))
        if 2 <= num_players <= 6 and cards_per_player > 0:
            play_game(num_players, cards_per_player)
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Please enter valid numbers.")

