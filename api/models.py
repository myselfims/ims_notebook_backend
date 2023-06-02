from django.db import models
from django.contrib.auth.models import User



class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    bookmark = models.BooleanField(default=False)
    
    def ___str__(self):
        return self.note
