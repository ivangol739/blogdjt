from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author'] #боковая модель с фильтрацией
    search_fields = ['title', 'body'] #Строка поиска
    prepopulated_fields = {'slug': ('title',)} #Автоматическое заполнение
    raw_id_fields = ['author'] #Поиск при выборе автора
    date_hierarchy = 'publish' #Навигационные ссылки, предназначенные для перемещения по иерархии дат, ниже поиска
    ordering = ['status', 'publish'] #упорядочивание по статусу

