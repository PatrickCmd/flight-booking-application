from django.conf import settings
from django.db import models


class PassportInfo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name="profiles",
                              on_delete=models.CASCADE)
    using_country = models.CharField(max_length=50, null=True)
    country_of_citizenship = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    issue_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    passport_photo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    class Meta:
        verbose_name = "Passport Information"

    def __str__(self):
        return self.passport_number
