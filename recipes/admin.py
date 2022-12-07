from django.contrib import admin
from .models import Recipe, RecipeIngredient


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    prepopulated_fields = {"slug": ('user', 'name',)}
    readonly_fields = ('created_at', 'updated_at')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient_name', 'recipe', 'get_recipe_user', 'quantity', 'unit')
    list_filter = ('recipe', 'unit', 'quantity')
    search_fields = ('recipe__name', 'name')
    list_display_links = ('ingredient_name', 'id')
    list_per_page = 50
    list_editable = ('unit', 'quantity',)
    search_help_text = 'shu yerdan qidir'
    date_hierarchy = 'created_at'
    autocomplete_fields = ('recipe',)

    def get_recipe_user(self, obj):
        return obj.recipe.user


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
