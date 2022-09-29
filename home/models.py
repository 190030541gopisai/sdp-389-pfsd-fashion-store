from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    #one to one cardinality 
    #when user deleted profile also gets deleted but when you delete profile
    #user is not deleted that is use of models.CASCADE
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepics/default.png',upload_to='profilepics')
 
    def __str__(self):
        return f'{self.user.username} Profile' #for display name in admin panel


