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
        ('State Bank of India', 'State Bank of India'),
        ('Punjab National Bank', 'Punjab National Bank'),
        ('Axis Bank', 'Axis Bank'),
        ('HDFC Bank', 'HDFC Bank'),
        ('Bank of Baroda', 'Bank of Baroda'),
        ('Canara Bank', 'Canara Bank'),
        ('ICICI Bank', 'ICICI Bank'),
        ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'),
        ('DCB Bank Hyderabad', 'DCB Bank Hyderabad'),
        ('IDBI Bank', 'IDBI Bank'),
        ('Andhra Bank', 'Andhra Bank'),
        ('Federal Bank', 'Federal Bank'),
        ('IndusInd Bank', 'IndusInd Bank'),
        ('Karnataka Bank', 'Karnataka Bank'),
        ('City Union Bank', 'City Union Bank'),
        ('UCO Bank', 'UCO Bank'),
        ('Karur Vysya Bank', 'Karur Vysya Bank'),
        ('RBL Bank', 'RBL Bank'),
        ('Yes Bank', 'Yes Bank'),
        ('Union Bank of India', 'Union Bank of India'),
        ('Auxillo Hyderabad', 'Auxillo Hyderabad'),
        ('Avanse', 'Avanse'),
        ('Gyan Dyaan', 'Gyan Dyaan'),
        ('Student Cover', 'Student Cover'),
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
    
    bank = models.TextField(max_length=100, choices=BANK, default="Choose Bank", null=True, blank = True)
    message = models.CharField(max_length=100, null=True, blank = True, default="NA")
    
    GOV_Status = models.TextField(max_length=100, choices=STATUS, default="Pending", null=True, blank = True)
    GOV_Bank = models.TextField(max_length=100, choices=BANK, default="Choose Bank", null=True, blank = True)
    GOV_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    GOV_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    SBI_Status = models.TextField(max_length=100, choices=STATUS, default="Pending", null=True, blank = True)
    SBI_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    SBI_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    PNB_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    PNB_Capital_Amount = models.IntegerField(null=True, blank = True , default="0")
    PNB_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True, default="0.0")
    
    Axis_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Axis_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Axis_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    HDFC_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    HDFC_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    HDFC_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    BOB_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    BOB_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    BOB_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Canara_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Canara_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Canara_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    ICICI_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    ICICI_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    ICICI_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Kotak_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Kotak_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Kotak_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    DCB_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    DCB_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    DCB_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    IDBI_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    IDBI_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    IDBI_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Andhra_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Andhra_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Andhra_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Federal_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Federal_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Federal_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    IndusInd_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    IndusInd_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    IndusInd_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Karnataka_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Karnataka_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Karnataka_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    City_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    City_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    City_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    UCO_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    UCO_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    UCO_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    KVB_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    KVB_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    KVB_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    RBL_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    RBL_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    RBL_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    YES_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    YES_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    YES_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Union_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Union_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Union_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Auxillo_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Auxillo_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Auxillo_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Avanse_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Avanse_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Avanse_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Gyan_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Gyan_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Gyan_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")
    
    Student_Status = models.TextField(max_length=100, choices=STATUS, default="Pending" , null=True, blank = True)
    Student_Capital_Amount = models.IntegerField(null=True, blank = True, default="0")
    Student_Interest = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank = True , default="0.0")

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
