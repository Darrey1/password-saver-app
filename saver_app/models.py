from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
class UserPW(models.Model):
    PW_TYPES = [('confidentail', 'confidentail'),('sharable', 'sharable')]
    title = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=PW_TYPES, max_length=12)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    
    def __str__(self):
        return self.title
    
