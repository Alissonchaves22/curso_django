from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'publicado', 'status']
    list_filter = ['criado', 'autor', 'publicado', 'status']
    date_hierarchy = "publicado"
    raw_id_fields = ("autor", )
    search_fields = ['titulo', 'conteudo']
    prepopulated_fields = {'slug': ('titulo',)}