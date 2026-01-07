from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
import re

def parse_hand(hand_string) :
    """Converts Hand String to Full Hand"""
    p1 = re.compile(".{26}")
    p2 = re.compile("..")
    args = [p2.findall(x) for x in p1.findall(hand_string)]
    if len(args) != 4 :
        raise ValidationError(_("Invalid Hand Input"))
    return Hand(**args)

class Person(models.Model) :
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Handfield(models.Field) :
    description = "A hand of cards (Bridge Style)"
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 104
        super().__init__(*args, **kwargs)
        
    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
    
    def from_db_value(self, value, expression, connection) :
        if value is None :
            return value
        return parse_hand(value)
    
    def to_python(self, value):
        if isinstance(value, Hand) :
            return value
        if value is None :
            return value
        return parse_hand(value)
    
    def get_prep_value(self, value) :
        return "".join(["".join(l) for l in (value.north, value.east, value.south, value.west)])
    
    def get_db_prep_save(self, value, connection, prepared = False) :
        value = super().get_db_prep_save(value, connection, prepared)
        if value is not None :
            return connection.Database.Binary(value)
        return value
    
    def get_internal_type(self):
        return "CharField"
    
    def value_to_string(self, obj) :
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
    
class Hand(models.Model) :
    hand = Handfield()