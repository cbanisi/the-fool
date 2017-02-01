
import unittest
from django.test import TestCase

from the_fool.models import TarotCard

class TarotCardTestCase(TestCase):
#    "Tests Tarot Card Deck Creation"
    
    def test_TarotCard_has_name(self):
        tarotCard = TarotCard("testCard")
        self.assertEquals(tarotCard.name,"testCard")
