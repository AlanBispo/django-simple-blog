from django.contrib import admin
from .models import Post, Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'criado_em')
    prepopulated_fields = {'slug': ('titulo',)}