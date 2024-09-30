from django.contrib import admin
from .models import Company, UploadedFile

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'year_founded', 'industry', 'locality', 'country', 'linkedin_url', 'employees_from', 'employees_to')
admin.site.register(Company, CompanyAdmin)

admin.site.register(UploadedFile)