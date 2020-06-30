from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
import uuid

# Create your models here.
from customers.models import CustomerDetails
from userManagement.models import User


class Receipts(models.Model):
    # signature
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_number = models.CharField(null=True, max_length=1000)  # need to customize this
    date = models.DateTimeField(null=True, default=datetime.now, blank=True)
    font = models.CharField(null=True, max_length=1000)
    color = models.CharField(null=True, max_length=1000)
    preset = models.BooleanField(null=True, default=False)
    paid_stamp = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    issued = models.BooleanField(null=True, default=False)
    deleted = models.BooleanField(null=True, default=False)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, null=False)


class Products(models.Model):
    receipt = models.ForeignKey(Receipts, on_delete=models.CASCADE, null=False)
    name = models.CharField(null=False, max_length=100)
    quantity = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    unit_price = models.FloatField(null=False, validators=[MinValueValidator(0)])
    part_payment = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    title = models.CharField(null=True, max_length=100)
    message = models.CharField(null=True, max_length=100)
    date_to_deliver = models.DateField(null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BusinessInfo(models.Model):
    name = models.CharField(null = False, unique= True, max_length=150)
    phone_number = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=200, null=False)
    slogan = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')