from django.contrib import admin
from .models import Patient, RiskPercentange

# Register your models here.
admin.site.register(Patient)
admin.site.register(RiskPercentange)
