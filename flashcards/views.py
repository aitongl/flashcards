from django.shortcuts import render
from flashcards.models import FlashcardSet, Card
from flashcards.forms import FlashcardSetForm, CardForm

# Create your views here.

def allSets(request):
    content = {}
    content['forms'] = FlashcardSetForm()
    return render(request, 'flashcards/allSets.html', content)

def addSet(request):
    if request.method == 'POST':
        form = FlashcardSetForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    return render(request, 'flashcards/allSets.html')