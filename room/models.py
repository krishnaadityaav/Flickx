from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    members = models.ManyToManyField(User,related_name='rooms',default=True)
    
class Open_room(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    open_room = models.ForeignKey(Open_room, related_name='messages', on_delete=models.CASCADE )
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
        
        

   
class JoinRequest(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('accepted', 'Accepted'),
        ('rejected','Rejected'),
        
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    

    def _str_(self):
        return f'{self.sender} - {self.room}'