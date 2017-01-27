from django.http import HttpResponse
from app.models import TarotCardDeck
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def deck(request):
    deck = TarotCardDeck();
    htmlResponse = ''
    for card in deck.shuffle():
        htmlResponse += card + "</br>"
    return HttpResponse(htmlResponse)