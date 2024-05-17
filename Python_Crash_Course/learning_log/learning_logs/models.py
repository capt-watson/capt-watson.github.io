from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """a Topic which user is learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  ## Foreign key links the User model to Owner. If user deleted, all topics of user will be deleted.
    
    def __str__(self):
        """Displays the entered text"""
        return self.text
    
class Entry(models.Model):
    """A specific entry in a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Display the entered text"""
        return f"{self.text[:50]}..."

