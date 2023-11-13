from django.db import models
#from accounts.models import CustomeUser
import datetime


    
    



class Chair(models.Model):
    image = models.ImageField(upload_to='chair',default='default.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    

    def snip(self):
        return self.content[:20] + '...'
    
    def capt(self):
        return self.title.capitalize()
    

