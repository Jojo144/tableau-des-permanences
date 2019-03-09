from django.db import models


class Activity(models.Model):
    class Meta:
        verbose_name = "Activité"
    description = models.CharField(max_length=200)
    date = models.DateField()
    volunteer1 = models.CharField(verbose_name='Permanencier 1', max_length=200, blank=True)
    volunteer2 = models.CharField(verbose_name='Permanencier 2', max_length=200, blank=True)
    comment = models.CharField(verbose_name='Commentaire', max_length=1000, blank=True)
    def __str__(self):
        return self.description
