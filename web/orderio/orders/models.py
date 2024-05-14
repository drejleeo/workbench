from django.db import models


class Order(models.Model):
    class Marketplace(models.TextChoices):
        AMAZON = "amazon", "amazon"
        CDISCOUNT = "cdiscount", "cdiscount"

    marketplace = models.CharField(choices=Marketplace.choices, max_length=55)
    order_id = models.CharField(null=True, blank=True, max_length=55)
    order_purchase_date = models.DateField(null=True, blank=True)
    order_purchase_heure = models.TimeField(null=True, blank=True)
    order_amount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=1)

    order_payment = models.OneToOneField('Payment', null=True, related_name='order', on_delete=models.CASCADE)
    billing_address = models.OneToOneField('BillingAddress', null=True, related_name='order', on_delete=models.CASCADE)
    tracking_informations = models.OneToOneField('Tracking', null=True, related_name='order', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='cart')


class Payment(models.Model):
    payment_type = models.CharField(null=True, max_length=55, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_heure = models.TimeField(null=True, blank=True)


class BillingAddress(models.Model):
    billing_society = models.CharField(null=True, blank=True, max_length=100)
    billing_email = models.EmailField(null=True)
    billing_address = models.CharField(null=True, max_length=200)
    billing_city = models.CharField(null=True, max_length=55)
    billing_country = models.CharField(null=True, max_length=55)
    billing_phone_office = models.CharField(null=True, max_length=55)

class Tracking(models.Model):
    tracking_method = models.CharField(null=True, blank=True, max_length=55)
    tracking_carrier = models.CharField(null=True, blank=True, max_length=55)
    tracking_number = models.CharField(null=True, blank=True, max_length=55)
    tracking_url = models.URLField(null=True, blank=True)


class Product(models.Model):
    title = models.CharField(null=True, max_length=100, blank=True)
    url_image = models.URLField(null=True)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=1)
    quantity = models.SmallIntegerField(blank=False, )