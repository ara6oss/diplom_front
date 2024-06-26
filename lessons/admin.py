from django.contrib import admin
from django import forms
from lessons.models import Category, Comment, Lesson, Module, Content
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class ContentInline(admin.StackedInline):
    model=Content

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['title', 'lesson']
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ['lesson']
    search_fields = ['title', 'lesson']
    inlines = [ContentInline]



class ModuleInline(admin.StackedInline):
    model=Module
    prepopulated_fields = {"slug": ('title',)}
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ('title',)}
    
    
class OverviewLessonForm(forms.ModelForm):
    overview = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdminForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Сначала сохраняем объект, чтобы получить значение id
        if commit:
            instance.save()
            self.save_m2m()  # Сохраняем многие ко многим связи
        return instance
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['title', 'category','owner', 'created']
    list_filter = ['created', 'category']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    form = OverviewLessonForm
    inlines = [ModuleInline]


admin.site.register(Content)
admin.site.register(Comment)