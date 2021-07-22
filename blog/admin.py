from django.contrib import admin
from .models import Post, Category
from social.models import Link


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado', 'publicado']
    list_filter = ['nome', 'criado', 'publicado']
    date_hierarchy = "publicado"
    search_fields = ['nome',]

    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'publicado', 'status']
    list_filter = ['criado', 'autor', 'publicado', 'status']
    readonly_fields = ('visualizar_imagem', )
    date_hierarchy = "publicado"
    raw_id_fields = ("autor", )
    search_fields = ['titulo', 'conteudo']
    prepopulated_fields = {'slug': ('titulo',)}

    def visualizar_imagem(self, obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem cadastrada" 


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    readonly_fields =('criado', 'publicado')
    list_display = ['chave', 'criado', 'publicado']
    
   
    
