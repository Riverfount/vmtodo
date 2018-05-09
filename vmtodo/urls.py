from django.contrib import admin
from django.urls import path

from vmtodo.core.views import get_post_tasks, get_delete_put_task_datail

urlpatterns = [
    path('api/v1/tasks/', get_post_tasks),
    path('api/v1/tasks/<int:pk>', get_delete_put_task_datail),
    path('admin/', admin.site.urls),
]
