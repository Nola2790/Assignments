from django.db import models

# Create your models here.

class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Recipient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_date = models.DateField()
    donation_location = models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        return f"Donation by {self.donor}"


# donor/models.py
class Branch(models.Model):
    name = models.CharField(max_length=100)
  
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='locations')
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    event_image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.name
class Feedback(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])

    def __str__(self):
        return f"Feedback from {self.donor.first_name} - Rating: {self.rating}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name