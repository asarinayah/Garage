from django.db import models
from django.utils import timezone
from decimal import Decimal

class vehicle(models.Model):
    owner_name=models.CharField(max_length=100)
    phone=models.CharField( max_length=10)
    plate=models.CharField(max_length=50,unique=True)
    make=models.CharField(max_length=50,blank=True)
    model=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.plate
    

class jobitem(models.Model):
    vehicle=models.ForeignKey(vehicle,on_delete=models.CASCADE,related_name="jobs")
    description=models.TextField()
    labor_hours=models.DecimalField( max_digits=5, decimal_places=2)
    labor_rate=models.DecimalField( max_digits=5, decimal_places=2)
    parts_cost=models.DecimalField( max_digits=5, decimal_places=2)
    created_at=models.DateTimeField(default=timezone.now)

    @property
    def total(self):
        return(self.labor_hours * self.labor_rate) + self.parts_cost
    

class invoice(models.Model):
    invoice_number=models.CharField(max_length=50,unique=True)
    vehicle=models.ForeignKey(vehicle,on_delete=models.SET_NULL,null=True)
    job_items = models.ManyToManyField(jobitem)
    issued_at = models.DateTimeField(default=timezone.now)
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)

    def subtotal(self):
        return sum(item.total for item in self.job_items.all())
    

    def tax_amount(self):
        return (self.subtotal() - self.discount) * (self.tax_percent / 100)

    def total_amount(self):
        return self.subtotal() - self.discount + self.tax_amount()