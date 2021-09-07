from django.contrib import admin
from .templates.models import students_model, groups_model


admin.site.register(students_model.Student)
admin.site.register(groups_model.Group)
