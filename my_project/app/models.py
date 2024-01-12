from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings

SECTION_CHOICES = (
    ('INTRO', 'Introduction'),
    ('SUP', 'Superposition'),
    ('QUB', 'Qubits'),
    ('MEA', 'Measurement'),
    ('CIR', 'Circuit'),
    ('ENT', 'Entanglement'),
    ('NOI', 'Noise'),
    ('CON', 'Control'),
    ('PRO', 'Programming')
)

class Section(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='sections/', blank=True, null=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    section = models.CharField(max_length=5, choices=SECTION_CHOICES, default='INTRO')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sections/', blank=True, null=True, verbose_name=_("Image"))
    text = models.TextField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s progress on {self.content}"
