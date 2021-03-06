from django.db import models
from django.contrib.auth.models import User

from uuid import uuid4

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # set the time to now only when the record is added to the database
    last_modified = models.DateTimeField(auto_now=True)  # will update anytime the record changes

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.id} {self.title}>'
        # return f'<Note: {self.id} {self.title}>'  # return format string for note title

class PersonalNote(Note):   # inherits from Note so as not to repeat the fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # user field
