from django.db import models

class Product(models.Model) :
    name = models.CharField(max_length = 100)
    
class Order(models.Model) :
    reference = models.CharField(max_length = 20, primary_key = True)
    
class OrderLineItem(models.Model) :
    pk = models.CompositePrimaryKey("product_id", "order_id")
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    
class ForiegnObjectExample(models.Model) :
    item_order_id = models.CharField(max_length = 20)
    item_product_id = models.IntegerField()
    item = models.ForeignObject(
        OrderLineItem,
        on_delete = models.CASCADE,
        from_fields = ("item_order_id", "item_product_id"),
        to_fields = ("order_id", "product_id")
    )

class Number(models.Model) :
    no = models.IntegerField()
    def __str__(self):
        return f'{self.no}'