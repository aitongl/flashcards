from django.shortcuts import render, redirect, get_object_or_404
from flashcards.models import FlashcardSet, Card
from flashcards.forms import FlashcardSetForm, CardForm

def allSets(request):
    content = {}
    content['forms'] = FlashcardSetForm()
    allSets = FlashcardSet.objects.all()
    content['sets'] = allSets
    return render(request, 'flashcards/allSets.html', content)

def addSet(request):
    if request.method == 'POST':
        form = FlashcardSetForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
    return allSets(request)

def viewSet(request, id):
    flashcard_set = get_object_or_404(FlashcardSet, id=id)
    flashcards = Card.objects.filter(set=flashcard_set)
    context = {'set': flashcard_set, 'flashcards': flashcards, 'form': CardForm()}
    return render(request, 'flashcards/viewSet.html', context)

def editSet(request, id):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False) 
            card.set = get_object_or_404(FlashcardSet, id=id)
            form.save()
    return viewSet(request, id=id) 

