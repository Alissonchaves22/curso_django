from django.db import models

class Link(models.Model):
    chave = models.SlugField(max_length=100, verbose_name="Identificação", unique=True)
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    url = models.URLField(max_length=200, null=False, blank=False)
    criado = models.DateField(auto_now_add=True)
    publicado = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"
        ordering = ["-chave"]
    
    def __str__(self):
        return self.chave