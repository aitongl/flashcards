from django.db import models

# Create your models here.

class FlashcardSet(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.title
    
class Card(models.Model):
    front = models.CharField(max_length=1000)
    back = models.CharField(max_length=1000)
    set = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE)
    def __str__(self):
        return self.front + " - " + self.back