# team/models.py
from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class TeamMember(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('regular', 'Regular')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(
            max_length=15,
            validators=[
                RegexValidator(
                    regex=r'^\d{10}$',  # Ensure phone number is exactly 10 digits
                    message='Phone number must be exactly 10 digits.',
                ),
            ],
        )
    email = models.EmailField(
        unique=True,  # Ensure email is unique
        validators=[EmailValidator(message='Enter a valid email address.')],
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        app_label = 'app' 
        ordering = ['id']  # Default ordering by ID 