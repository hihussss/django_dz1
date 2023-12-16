from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope



class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            tag = form.cleaned_data.get('tag')
            if Tag.objects.filter(name=tag).exists():
                raise ValidationError('Такой тег уже привязан к разделу')      
        return super().clean()  # вызываем базовый код переопределяемого метода
class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
