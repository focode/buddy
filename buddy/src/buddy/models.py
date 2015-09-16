from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class usersProfiles(models.Model):
  username = models.CharField(max_length=100)
  age = models.IntegerField(max_length=100)
  email = models.EmailField()
  gender = models.CharField(max_length=100)
  address = models.TextField(max_length=500)
  ethenic = models.CharField(max_length=100)
  interest = models.TextField(max_length=500)




  #Copied from : http://code.runnable.com/UqK6IqmXsSAmAAb2/t-shirt-registration-form-using-django-modelform-for-python
