from django.db import models

class Topic(models.Model):
    nom = models.CharField(max_length=150)
    def __str__(self): return self.nom


class Audio(models.Model):
    name = models.CharField(max_length=300)
    file = models.FileField(null=True, upload_to="audios")
    rn = models.PositiveIntegerField(default=1)
    duration = models.DurationField(null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    def __str__(self): return self.name
