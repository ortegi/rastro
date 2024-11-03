from django.contrib import admin
from .models import Article, Category
from django import forms
from firebase_admin import storage
from .utils import upload_image_to_firebase
# Register your models here.

#admin.site.register(Article)



class ArticleAdminForm(forms.ModelForm):
   image_file = forms.FileField(required=False)  # File input for image upload

   class Meta:
       model = Article
       fields = ['title', 'description', 'price', 'category']  # Include any fields you need

   def save(self, commit=True):
       instance = super().save(commit=False)

       # Get the image file from the form
       image_file = self.cleaned_data.get('image_file')
       if image_file:
           # Upload to Firebase and get the public URL
           image_url = upload_image_to_firebase(image_file)
           # Save the URL in the model instance
           instance.image_url = image_url

       if commit:
           instance.save()
       return instance
   
   
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'state', 'image_url')
    list_filter = ('category', 'state')
    form = ArticleAdminForm
           

admin.site.register(Article, ArticleAdmin)
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', id)    
    