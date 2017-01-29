
from random import randint

class TarotCardDeck():

    def __init__(self):
        self.deck = [
                TarotCard("Fool"),
                TarotCard("Magician"),
                TarotCard("Priestess"),
                TarotCard("Empress"),
                TarotCard("Emperor"),
                TarotCard("Hierophant"),
                TarotCard("Lovers"),
                TarotCard("Chariot"),
                TarotCard("Strength"),
                TarotCard("Hermit"),
                TarotCard("Fortune"),
                TarotCard("Justice"),
                TarotCard("Hangedman"),
                TarotCard("Death"),
                TarotCard("Temperance"),
                TarotCard("Devil"),
                TarotCard("Tower"),
                TarotCard("Star"),
                TarotCard("Moon"),
                TarotCard("Sun"),
                TarotCard("Judgement"),
                TarotCard("World")
            ];

    def shuffle(self):
        
        for currentIndex, card in enumerate(self.deck):

            randomIndex = randint(currentIndex,len(self.deck) - 1)
            #swap current index and the randomIndex
            temp = self.deck[randomIndex]
            self.deck[randomIndex] = self.deck[currentIndex]
            self.deck[currentIndex] = temp

        return self.deck

class TarotCard():
    def __init__(self, name):
        self.name = name