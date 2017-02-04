
import unittest
from django.test import TestCase

from the_fool.models import TarotCardDeck

class TarotCardDeckTestCase(TestCase):
#    "Tests Tarot Card Deck Creation"
    
    def test_you_can_create_TarotCardDeck(self):
        tarotCardDeck = TarotCardDeck()
        self.assertEqual(22,len(tarotCardDeck.deck))

    def test_shuffle_returns_deck(self):
        tarotCardDeck = TarotCardDeck()
        self.assertEqual(len(tarotCardDeck.shuffle()),22)

    def test_card_names_are_unique(self):
        tarotCardDeck = TarotCardDeck()
        name_set = set()
        for card in tarotCardDeck.deck:
            name_set.add(card.name)
        self.assertEqual(len(name_set),22)

    def test_card_definitions_are_unique(self):
        tarotCardDeck = TarotCardDeck()
        description_set = set()
        for card in tarotCardDeck.deck:
            description_set.add(card.description)
        self.assertEqual(len(description_set),22)