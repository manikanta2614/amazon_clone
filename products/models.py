from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.CharField(max_length=100)

    stock = models.IntegerField()

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

class Order(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    quantity = models.IntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    order_date = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=50,
        default='Pending'
    )

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"