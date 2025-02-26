from Deck import MultiDeck
from Card import Face
class Game():
    def __init__(self):
        self.multideck=MultiDeck()
        self.deck_count=self.multideck.deck_count
        print(f"Using {self.deck_count} decks.")
        self.player_hand=[]
        self.dealer_hand=[]
        self.player_hand.append(self.multideck.DrawRand())
        self.player_hand.append(self.multideck.DrawRand())
        self.dealer_hand.append(self.multideck.DrawRand())
        self.dealer_hand.append(self.multideck.DrawRand())
    def hit(self, hand):
        hand.append(self.multideck.DrawRand())
    def hand_tot(self, hand):
        total=0
        ace_count=0
        for card in hand:
            total+=card.face.face_value()
            if card.face == Face.ACE:
                ace_count +=1
        while total > 21 and ace_count > 0: #changes value of Aces if tot >21
            total -=10 #turns ace into 1 instead of 11
            ace_count -=1
        return total
    def start_game(self):
        while True:  
            print("Welcome to BlackJack!")
            # Show the player's and dealer's starting hands
            print(f"Your hand: {', '.join(str(card) for card in self.player_hand)} (Total: {self.hand_tot(self.player_hand)})")
            print(f"Dealer's hand: {self.dealer_hand[0]} [HIDDEN]")

            # Player's turn
            while self.hand_tot(self.player_hand) <= 21:
                response = input("Do you want to Hit or Stay? ").lower()

                #  input response
                if response == "hit":
                    self.hit(self.player_hand)
                    print(f"You drew: {self.player_hand[-1]}")
                    print(f"Your hand: {', '.join(str(card) for card in self.player_hand)} (Total: {self.hand_tot(self.player_hand)})")

                    if self.hand_tot(self.player_hand) > 21:
                        print("You busted! Your total exceeds 21.")
                        return  # End the game since the player busts

                elif response == "stay":
                    break  # Player decides to stay

                else:
                    print("Invalid input. Please enter 'Hit' or 'Stay'.")
            
            # Dealer's turn (Dealer must hit until at least 17)
            print(f"Dealer reveals their hand: {', '.join(str(card) for card in self.dealer_hand)} (Total: {self.hand_tot(self.dealer_hand)})")

            while self.hand_tot(self.dealer_hand) < 17:
                self.hit(self.dealer_hand)
                print(f"Dealer drew: {self.dealer_hand[-1]}")
                print(f"Dealer's hand: {', '.join(str(card) for card in self.dealer_hand)} (Total: {self.hand_tot(self.dealer_hand)})")

            # determines the winner
            player_total = self.hand_tot(self.player_hand)
            dealer_total = self.hand_tot(self.dealer_hand)

            if player_total > 21:
                print("You busted! You lose.")
            elif dealer_total > 21:
                print("Dealer busted! You win!")
            elif player_total > dealer_total:
                print(f"You win! Your total: {player_total}, Dealer's total: {dealer_total}")
            elif player_total < dealer_total:
                print(f"You lose. Your total: {player_total}, Dealer's total: {dealer_total}")
            else:
                print(f"It's a tie! Your total: {player_total}, Dealer's total: {dealer_total}")
            
            # Ask player if they want to play again
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Game Over: Thanks for playing!")
                break  # End the game
            else:
                #this will reset the state of the game
                self.player_hand.clear()
                self.dealer_hand.clear()
                self.player_hand.append(self.multideck.DrawRand())
                self.player_hand.append(self.multideck.DrawRand())
                self.dealer_hand.append(self.multideck.DrawRand())
                self.dealer_hand.append(self.multideck.DrawRand())