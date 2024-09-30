from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(("name"), max_length=250,  db_index=True)
    domain = models.CharField(("domain"), max_length=200)
    year_founded = models.CharField(("year founded"), max_length=20,  db_index=True)
    industry = models.CharField(("industry"), max_length=250,  db_index=True)
    locality = models.CharField(("locality"), max_length=250, null=True,  blank=True,  db_index=True)
    country = models.CharField(("country"), max_length=250, null=True,  blank=True,  db_index=True)
    linkedin_url = models.CharField(("linkedin url"), max_length=250, null=True, blank=True)
    employees_from = models.CharField(("employees_from"), max_length=250, null=True, blank=True,  db_index=True)
    employees_to = models.CharField(("employees_to"), max_length=250, null=True, blank=True,  db_index=True)
    
    class meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name
    
    class meta:
        verbose_name = ("Uploaded File")
        verbose_name_plural = ("Uploaded Files")