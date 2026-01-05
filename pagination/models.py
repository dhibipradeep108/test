from django.db import models

class Contact(models.Model) :
    name = models.CharField(max_length = 40)
    phno = models.DecimalField(max_digits = 12, decimal_places = 0, unique = True)
    def __str__(self):
        return f'{self.name} : {self.phno}'