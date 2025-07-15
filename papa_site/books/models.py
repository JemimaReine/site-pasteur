from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    couverture = models.ImageField(upload_to='livres/', null=True, blank=True)
    resume = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titre

class Commande(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenoms} - {self.livre.titre}"
