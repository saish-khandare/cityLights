from django.db import models



class User(models.Model):
    userid = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    code = models.IntegerField(default=0)



    class Meta:
        db_table = 'user'
