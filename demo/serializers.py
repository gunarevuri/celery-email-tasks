from rest_framework.serializers import ModelSerializer

from .models import Task_tracker, Task, Update_type

class TaskSerializer(ModelSerializer):
	"Model serializers which serializes Task model"
	class Meta:
		model = Task
		fields = ['task_type', 'task_desc']


class TaskTrackerSerializer(ModelSerializer):
	"Model serializers which serializes Task_tracker model"
	class Meta:
		model = Task_tracker
		fields = '__all__'

class UpdateTypeSerializer(ModelSerializer):
	class Meta:
		model = Update_type
		fields = '__all__'