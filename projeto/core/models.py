from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
	created = models.DateTimeField(
			'criado em',
			auto_now_add=True,
			auto_now=False
		)

	modified = models.DateTimeField(
			'modificado em',
			auto_now_add=False,
			auto_now=True
		)

	class Meta:
		# Usar classe como herança de classe em outros Models
		abstract = True