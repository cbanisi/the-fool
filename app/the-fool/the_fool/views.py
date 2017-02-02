from django.http import HttpResponse
from the_fool.models import TarotCardDeck
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def deck(request):
    deck = TarotCardDeck();
    htmlResponse = ''
    for card in deck.shuffle():
        htmlResponse += card.name + "</br>"
    return HttpResponse(htmlResponse)

def game(request):
    deck = TarotCardDeck()
    htmlResponse = ''
    shuffledDeck = deck.shuffle()[:5]
    for card in shuffledDeck:
        htmlResponse += card.name + ": " + card.description + "</br>"
    return HttpResponse(htmlResponse)