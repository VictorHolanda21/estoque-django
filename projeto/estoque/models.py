from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import TimeStampedModel
from projeto.produto.models import Produto
from .managers import EstoqueEntradaManager, EstoqueSaidaManager

# Create your models here.

MOVIMENTO = (
		('e', 'entrada'),
		('s', 'saida'),
	)

class Estoque(TimeStampedModel):
	funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
	nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
	movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		if self.nf:
			return '{} - {} - {}'.format(self.pk, str(self.nf).zfill(3), self.created.strftime('%d-%m-%Y'))
		return '{} --- {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

	def nf_formated(self):
		if self.nf:
			return str(self.nf).zfill(3)
		return '---'

	# def get_absolute_url(self):
	# 	return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})

class EstoqueEntrada(Estoque):

	objects = EstoqueEntradaManager()

	class Meta:
		proxy=True
		verbose_name='estoque entrada'
		verbose_name_plural='estoque entradas'

	def get_absolute_url(self):
		return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})



class EstoqueSaida(Estoque):

	objects = EstoqueSaidaManager()

	class Meta:
		proxy=True
		verbose_name='estoque saida'
		verbose_name_plural='estoque saidas'

	def get_absolute_url(self):
		return reverse_lazy('estoque:estoque_saida_detail', kwargs={'pk': self.pk})


class EstoqueItens(models.Model):
	estoque = models.ForeignKey(
			Estoque, 
			on_delete=models.CASCADE,
			related_name='estoques')
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	quantidade = models.PositiveIntegerField()
	saldo = models.PositiveIntegerField()

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
		
		
			


