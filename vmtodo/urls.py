from django.contrib import admin
from django.urls import path

from vmtodo.core.views import get_post_tasks, get_delete_put_task_detail
from vmtodo.drf.views import TaskList, TaskDetails

urlpatterns = [
    path('drf/api/v1/tasks/', TaskList.as_view()),
    path('drf/api/v1/tasks/<int:pk>', TaskDetails.as_view()),
    path('api/v1/tasks/', get_post_tasks),
    path('api/v1/tasks/<int:pk>', get_delete_put_task_detail),
    path('admin/', admin.site.urls),
]
