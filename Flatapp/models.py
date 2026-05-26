from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((1, "Active"), (2, "Inactive"))
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    aadhar = models.CharField(max_length=100, null=True, blank=True)
    sec_question = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    aadhar_img = models.FileField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

STATUS = ((1, "Active"), (2, "Inactive"))
class Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    elect_img = models.FileField(null=True, blank=True)
    sec_question = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    aadhar_img = models.FileField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=2)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

STATUS = ((1, "Active"), (2, "Deactivate"))
class Apartment(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    furnish = models.CharField(max_length=200, null=True, blank=True)
    atype = models.CharField(max_length=200, null=True, blank=True)
    ebill = models.CharField(max_length=200, null=True, blank=True)
    extra = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    rent = models.CharField(max_length=200, null=True, blank=True)
    pic1 = models.FileField(null=True, blank=True)
    pic2 = models.FileField(null=True, blank=True)
    pic3 = models.FileField(null=True, blank=True)
    pic4 = models.FileField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.user.first_name

class Feedback(models.Model):
    register = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.register.user.first_name

class Payment(models.Model):
    register = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    apart = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True)
    cardno = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=100, default="Booking Amount", null=True, blank=True)
    nameoncard = models.CharField(max_length=100, null=True, blank=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, default="Booked", null=True, blank=True)
    bookingdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.apart.name


