from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

class Application(models.Model):
    COURSES = (
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    
    BANK = (
        ('SBI', 'SBI'),
        ('PNB', 'PNB'),
        ('Axis', 'Axis'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    ms_Course = models.CharField(max_length=200, choices= COURSES)
    name = models.CharField(max_length=200) 
    email = models.EmailField(max_length=200) 
    phone_no = models.CharField(max_length=200) 
    address = models.CharField(max_length=200) 
    profile_Picture = models.ImageField(upload_to="images") 
    Highschool_Percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    Highschool_Marksheet = models.ImageField(upload_to="images", null=True)
    Highschool_Passing_Certificate = models.ImageField(upload_to="images", null=True)
    identity_Proof = models.ImageField(upload_to="images", null=True)
    intermediate_Percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    intermediate_Marksheet = models.ImageField(upload_to="images", null=True)
    intermediate_Passing_Certificate = models.ImageField(upload_to="images", null=True)
    bank_Passbook = models.ImageField(upload_to="images", null=True)
    gRE_Score = models.IntegerField(null=True)
    gRE_Scorecard = models.ImageField(upload_to="images", null=True)
    iELTS_Score = models.IntegerField(null=True)
    iELTS_Scorecard = models.ImageField(upload_to="images", null=True)
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending",  blank=True)
    Bank = models.TextField(max_length=100, choices=BANK, default=" ", blank=True)
    Capital_Amount = models.IntegerField(null=True)
    Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    message = models.CharField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users')

class Notice(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Detail(models.Model):
    title = models.ForeignKey(Notice, on_delete=models.CASCADE)
    notice = models.CharField(max_length=200)

    def __str__(self):
        return self.notice
