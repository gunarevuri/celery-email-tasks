from django.shortcuts import render
import json
from django.http import HttpResponse

from .tasks import sleepy, send_email_task, send_tasks
from .models import Task_tracker, Task, Update_type
from .serializers import TaskSerializer, TaskTrackerSerializer,UpdateTypeSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from django.core import serializers as core_serializers

from demo.tasks import send_email_every_day_task

def index(request):
	send_email_task.delay()
	return HttpResponse("<h1>All done well Email has been sent</h1>")

# def send_email_view(request):
# 	
class TaskList(APIView):
	def get(self, request):
		tasks = Task.objects.all()
		serializer = TaskSerializer(tasks, many = True)
		return Response(serializer.data)

	def post(self, request):
		serializer = TaskSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			tasks = Task.objects.all()
			all_serializer = TaskSerializer(tasks, many = True)
			return Response(all_serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskTrackerList(APIView):
	def get(self, request):
		task_trackers = Task_tracker.objects.all()
		serializer = TaskTrackerSerializer(task_trackers, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK )

	def post(self, request):
		serializer = TaskTrackerSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class GetSpecificTasks(APIView):
	def get(self, request, type_id):
		tasks = Task.objects.filter(task_type =type_id).all()

		serializer = TaskSerializer(tasks, many = True)
		return Response(serializer.data, status=status.HTTP_200_OK)

def send_email_every_day_task_view(request):

	send_email_every_day_task.delay()
	return HttpResponse("<h1>done</h1>")







