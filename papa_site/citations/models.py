from django.db import models

class Citation(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date = models.DateField()
    video_url = models.URLField(blank=True, null=True, help_text="Lien YouTube ou autre")
    video_fichier = models.FileField(upload_to='videos/', blank=True, null=True, help_text="Ou téléversez une vidéo")


    def __str__(self):
        return f"{self.titre} - {self.date}"

    @property
    def video_embed_url(self):
        if self.video_url and 'youtube.com/watch?v=' in self.video_url:
            return self.video_url.replace('watch?v=', 'embed/')
        return self.video_url