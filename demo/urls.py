from django.urls import path

from demo import views

urlpatterns = [
		path('send_main', views.index, name="index"),
		path('get_tasks/', views.TaskList.as_view(), name='get_tasks'),
		path('get_task_trackers/', views.TaskTrackerList.as_view(), name='get_task_trackers'),
		path('tasks/<int:type_id>/', views.GetSpecificTasks.as_view(), name='tasks'),
# check whether tasks working or not manually
		path('send_tasks/', views.send_email_every_day_task_view, name='send_email_every_day_task_view'),
]