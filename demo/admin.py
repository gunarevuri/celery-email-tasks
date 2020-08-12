from django.contrib import admin
from .models import Task, Task_tracker, Update_type

admin.site.register(Task)

admin.site.register(Task_tracker)

admin.site.register(Update_type)

