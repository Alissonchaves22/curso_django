from django import forms
from django.db import models
from django.forms import ModelForm, fields
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('titulo', 'conteudo', 'status', 'categoria', 'imagem')

"""
STATUS = (
        ("rascunho", "Rascunho"),
        ("publicado", "Publicado")
        )
    
    titulo = models.CharField(max_length=250, verbose_name="Título")
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = RichTextField(verbose_name="Conteúdo")
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                            choices = STATUS, default="rascunho"
    )
    categoria = models.ManyToManyField(Category, related_name='get_posts' )
    imagem = models.ImageField(upload_to="blog", blank=True, null=True)

"""