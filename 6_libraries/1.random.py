import random
# <random.choice()>
coin = random.choice(["Heads", "Tails"])
print(coin)
# ----------------------------------------

#<random.randint()>
number = random.randint(1,10)
print(number)

# ----------------------------------------

#<random.shuffle>
cards = ["jack", "Queen", "king"]
random.shuffle(cards)

#prints current card
for card in cards:
    print(card)
# ----------------------------------------

