#generates a list of lists where each item represents a card and the corresponding value
#I realize this adds complexity but the code is more flexible in case I want to build 
#other card games in the future with more complicated scoring
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
import time

suits = "\u2660 \u2665 \u2666 \u2663".split()
ranks = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
deck = []

for suit in suits:
  for rank in ranks:
    if rank in "2,3,4,5,6,7,8,9,10":
      value = eval(rank)
    elif rank  == "A":
      value = 11
    else:
      value = 10
    card = [rank+suit,value]
    deck.append(card)

#used 6 decks to prevent counting when multiple hands are played with the same shuffle
decks = deck*6
random.shuffle(decks)

print("")
print ("***********************BLACKJACK***********************")
print("")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I made a few small changes. The instructions say to deal the first two cards to the
# player, but in a real game the cards are dealt one at a time so I made them alternate
# I also made the dealer's second card face up 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dealHand(): #this is the main function

# these functions within the main function imitate actions needed in a blackjack game
  def dealCard(player): #takes the first card in the shuffled decks, appends it to the player's hand and removes it from the deck
    topCard = decks.pop(0)
    player.append(topCard)

  def score(player): #calculates the score for the player passed as the single parameter
    total = 0
    for i in player:
      total += i[1]
    return total

  def showUsersHand(player): #tells the player their current hand and its total value
    showing = []
    for i in player:
      showing.append(i[0])
    print ("Your hand: ")
    time.sleep(1)
    print (showing)
    print ("Your total is ",score(player))
    print ("...")
    time.sleep(1)

  def showDealersHand(): #tells the player the dealer's hand and its total value
    showing = []
    for i in dealer:
      showing.append(i[0])
    time.sleep(1)
    print ("dealer has:")
    time.sleep(1)
    print (showing)
    print ("...")

  def playAgain(): #asks the user if they want to play again and reinitiates the game
    again = input("Would you like to play another hand? (y/n)").lower()
    if again == 'y':
      time.sleep(1)
      print ()
      print ("************************NEW HAND***********************")
      print ()
      time.sleep(1)
      dealHand()
    elif again == 'n':
      print("Thank you for playing")
    else:
      playAgain()

  def dealOut(): #dealer plays his hand out until he has 17 or busts
    showDealersHand()
    game = True
    while game:
      while score(dealer) < 17:
        print ("Dealer draws...")
        time.sleep(1)
        print (decks[0][0])
        dealCard(dealer)
      time.sleep(1)
      print ("Dealer has a total of ",score(dealer))
      print ("")
      if score(dealer) > 21:
        print ("Dealer busts. You win!")
        game = False
      elif score(user) > score(dealer):
        print ("You win!")
        game = False
      elif score(user) == score(dealer):
        print ("Push")
        game = False
      else:
        print ("Sorry, dealer wins :(")
        game = False
    playAgain()

  def hit():
    toHit = input("Would you like to hit or stay? (h/s)").lower()
    if toHit == 'h':
      print ("You draw...")
      time.sleep(1)
      print (decks[0][0])
      dealCard(user)
      showUsersHand(user)
      if score(user) == 21:
        print ("21. Perfect!")
        dealOut()
      elif score(user) > 21:
        print ("Sorry, too many. You lose :(")
        playAgain()
      else:
        hit()
    elif toHit == 's':
      dealOut()
    else:
      print ("Please enter h to hit or s to stay")
      hit()

# # This is where the "hand" actually starts. Each player's cards are cleared and
# new ones are dealt from the top of the deck.  This SHOULD have logic to auto-
# matically shuffle the decks whenever the decks get down to ~20% of the 
# original length of the deck but I highly doubt anybody playing this game
# will have the patience to get through 312 cards
  user = []
  dealer = []
  dealCard(user)
  dealCard(dealer)
  dealCard(user)
  dealCard(dealer)
  showUsersHand(user)
  print("Dealer shows ",dealer[1][0])
  print ("...")
  print ()
  if score(user) == 21 and score(dealer) == 21:
    print ("Push. Player and dealer both have 21")
    playAgain()
  elif score(user) == 21:
    print ("Blackjack! you win!")
    playAgain()
  else:
    hit()

#calls the function to start the game
dealHand()


