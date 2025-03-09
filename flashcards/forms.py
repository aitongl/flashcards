from django import forms

from flashcards.models import FlashcardSet, Card

class FlashcardSetForm(forms.ModelForm):
    class Meta:
        model = FlashcardSet
        fields = ('title', 'description')
        widgets = {
            'title': forms.Textarea(attrs={'id': 'set-title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'id': 'set-description', 'class': 'form-control', 'rows':3})
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('front', 'back')
        widgets = {
            'front': forms.Textarea(attrs={'id': 'card-front', 'class': 'form-control', 'rows':3}),
            'back': forms.Textarea(attrs={'id': 'card-back', 'class': 'form-control', 'rows':3}),
        }
        labels = {
            'front': 'Front',
            'back': 'Back',
        }
        