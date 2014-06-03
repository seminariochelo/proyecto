from django.db import models

class articulo(models.Model):
	titulo=models.CharField(max_length=100)
	descripcion=models.TextField()
	fecha=models.DateField()
	hora= models.TimeField()
	def __unicode__(self):
		return '%s%s'%(self.titulo,self.descripcion)
class comentario(models.Model):
	idAr=models.ForeignKey(articulo)
	Descripcion=models.TextField(max_length=100)
	fecha=models.DateField()
	def __unicode__(self):
		return '%s%s'%(self.Descripcion,self.fecha)

