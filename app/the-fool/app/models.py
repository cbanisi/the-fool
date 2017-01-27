#import collections
from random import randint

class TarotCardDeck():

    def __init__(self):
        self.deck = [
                "Fool",
                "Magician",
                "Priestess",
                "Empress",
                "Emperor",
                "Hierophant",
                "Lovers",
                "Chariot",
                "Strength",
                "Hermit",
                "Fortune",
                "Justice",
                "Hangedman",
                "Death",
                "Temperance",
                "Devil",
                "Tower",
                "Star",
                "Moon",
                "Sun",
                "Judgement",
                "World"
            ];

    def shuffle(self):
        
        for currentIndex, card in enumerate(self.deck):

            randomIndex = randint(currentIndex,len(self.deck) - 1)
            print(randomIndex)
            #swap current index and the randomIndex
            temp = self.deck[randomIndex]
            self.deck[randomIndex] = self.deck[currentIndex]
            self.deck[currentIndex] = temp

        return self.deck