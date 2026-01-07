from django.db import models
from django.db.models import Lookup, Field, Transform, IntegerField, FloatField, CharField, TextField

@Field.register_lookup
class NotEqual(Lookup) :
    lookup_name = "ne"
    def as_sql(self, compiler, connection):
        lhs, lhs_param = self.process_lhs(compiler, connection)
        rhs, rhs_param = self.process_rhs(compiler, connection) 
        params = lhs_param + rhs_param
        return "%s <> %s" % (lhs, rhs), params

@FloatField.register_lookup
@IntegerField.register_lookup
class AbsoluteValue(Transform) :
    lookup_name = 'abs'
    function = "ABS"
    @property
    def output_field(self) :
        return FloatField()

@AbsoluteValue.register_lookup
class AbsoluteValueLessThan(Lookup) :
    name = 'lt'
    def as_sql(self, compiler, connection) :
        lhs, lhs_param = compiler.compile(self.lhs.lhs)
        rhs, rhs_param = self.process_rhs(compiler, connection) 
        params = lhs_param + rhs_param + lhs_param + rhs_param
        return "%s < %s AND %s > -%s" % (lhs, rhs, lhs, rhs), params

@CharField.register_lookup
@TextField.register_lookup
class UpperCase(Transform) :
    lookup_name = 'upper'
    function = "UPPER"
    bilateral = True

class Number(models.Model) :
    no = models.FloatField(default = 0)
    def __str__(self):
        return f'{self.no}'
    
class Contact(models.Model) :
    name = models.CharField(max_length = 40)
    phno = models.DecimalField(max_digits = 12, decimal_places = 0, unique = True)
    def __str__(self):
        return f'{self.name} : {self.phno}'