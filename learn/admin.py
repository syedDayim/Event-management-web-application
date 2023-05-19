from django.contrib import admin
from .models import Course
# Register your models here.
@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'cover', 'title', 'bio', 'link')