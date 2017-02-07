
from random import randint
import yaml

class TarotCardDeck():

    def __init__(self):
        self.deck = []

        with open('the_fool/data/tarotCards.yml', 'r') as stream:
            doc = yaml.load(stream)
            
            for card in doc['cards']:
                cardKey = next(iter(card))
                self.deck.append(TarotCard(card[cardKey]['name'], card[cardKey]['description']))

    def shuffle(self):
        
        for currentIndex, card in enumerate(self.deck):

            randomIndex = randint(currentIndex,len(self.deck) - 1)
            #swap current index and the randomIndex
            temp = self.deck[randomIndex]
            self.deck[randomIndex] = self.deck[currentIndex]
            self.deck[currentIndex] = temp

        return self.deck

class TarotCard():
    def __init__(self, name, description):
        self.name = name
        self.description = description