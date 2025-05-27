from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    owner_address = models.TextField(blank=True, null=True)
    shop_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Rent(models.Model):
    MONTH_CHOICES = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    year = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.shop.name} - {self.get_month_display()} {self.year}"
