from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Coment(models.Model):
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    coment = models.CharField(max_length=50)
    descri = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.coment

    class Meta:
        permissions = (
            ('Usuario',_('Es profesor')),
            ('adm',_('Es adm')),
        )

class Recup(models.Model):
    user= models.CharField(max_length=50)
    passs= models.CharField(max_length=50)

    def __str__(self):
        return self.passs