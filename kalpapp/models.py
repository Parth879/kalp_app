from django.db import models

# Create your models here.

class Number(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=15)
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.number

class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.ForeignKey(Number,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    number = models.ForeignKey(Number,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    number = models.ForeignKey(Number,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    city = models.CharField(max_length=100,blank=True, null=True)
    join_date = models.DateField()
    expire_date = models.DateField()

    def __str__(self):
        return self.name