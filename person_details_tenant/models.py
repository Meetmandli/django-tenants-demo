from django.db import models
from person_details_shared.models import Person

class Person2(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name