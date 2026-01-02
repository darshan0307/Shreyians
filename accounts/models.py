from django.db import models

# Create your models here.

from django.db import models
class UserLogin(models.Model):
    mobile = models.CharField(max_length=15)
    login_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mobile

