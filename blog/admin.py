from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

from .models import * 

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'
        
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ("title",)}
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
