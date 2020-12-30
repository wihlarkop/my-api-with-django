from django.db import models


class Contact(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE)
    photo_profile = models.ImageField(upload_to='photo_profile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
