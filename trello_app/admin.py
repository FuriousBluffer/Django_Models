from django.contrib import admin
from trello_app import models
# Register your models here.


admin.site.register(models.Task)
admin.site.register(models.TaskList)
