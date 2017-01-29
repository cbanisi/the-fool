
import unittest
from django.test import TestCase

from the_fool.models import TarotCardDeck

class TarotCardDeckTestCase(TestCase):
#    "Tests Tarot Card Deck Creation"
    
    def test_you_can_create_TarotCardDeck(self):
        tarotCardDeck = TarotCardDeck()
        self.assertEquals(22,len(tarotCardDeck.deck))

    def test_shuffle_returns_deck(self):
        tarotCardDeck = TarotCardDeck()
        self.assertEqual(len(tarotCardDeck.shuffle()),22)