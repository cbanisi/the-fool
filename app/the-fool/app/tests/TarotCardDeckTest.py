import unittest

from app.models import TarotCardDeck

class TarotCardDeckTest(unittest.TestCase):
    "Tests Tarot Card Deck Creation"

    def can_create_TarotCardDeck(self):
        tarotCardDeck = TarotCardDeck()
        self.assertEquals(22,len(tarotCardDeck.deck))
        

    def test_basic_2(self):
        a = 1
        assert a == 1