from django.db import models

# Create your models here.


class TempsModel(models.Model):
	date_creation = models.DateTimeField(auto_now_add=True)
	date_de_mise_a_jour = models.DateTimeField(auto_now=True)


	class Meta:
		abstract = True



class Article(TempsModel):
	titre = models.CharField(max_length=255)
	contenu = models.TextField()	


	def __str__(self):
		return self.titre