from django.db import models

# Create your models here.
class Myweb(models.Model):
    아이디 = models.CharField(max_length= 45, blank=False, null=False)
    암호 = models.CharField(max_length= 10, blank=False, null=False)
    이름 = models.CharField(max_length= 5, blank=False, null=False)
    전화번호 = models.CharField(max_length= 20, blank=False, null=False)
    생년월일 = models.DateTimeField(null=False)
    이메일 = models.CharField(max_length= 45, blank=False, null=False)

    def __str__(self):
        return self.아이디