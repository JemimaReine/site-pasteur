from django.db import models

class Pasteur(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pasteur/', blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.nom

class PenseeDuJour(models.Model):
    date = models.DateField(auto_now_add=True)
    texte = models.TextField()
    video = models.URLField(blank=True, null=True)  # lien vers une vidéo YouTube, par exemple

    def __str__(self):
        return f"Pensee du {self.date}"

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')
    legende = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.legende or f"Image {self.id}"
