from django.db import models

# Create your models here.


class MyBuget(models.Model):
    total = models.IntegerField('total',default=0)
    spent = models.IntegerField('spent',default=0)
    actions = models.IntegerField('actions',default=0)

    def __str__(self):
        return str(self.total)


class Plans(models.Model):
    name = models.CharField('name', max_length=150)
    comment = models.CharField('comment', max_length=450)
    spent = models.IntegerField('spent money')
    payed = models.BooleanField('payed/not payed',default=False)

    def __str__(self):
        return self.name
    
    