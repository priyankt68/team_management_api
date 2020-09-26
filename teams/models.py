from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    role = models.CharField(choices=[("admin", "Admin"), ("regular", "Regular")], max_length=10)

    @property
    def fullname(self):
        return self.first_name + self.last_name
    
    def __unicode__(self):
        return self.first_name + self.last_name
    

