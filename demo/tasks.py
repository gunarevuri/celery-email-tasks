from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail
from time import sleep
from .models import Task, Task_tracker , Update_type

from django.core import serializers as core_serializers
import json
from django.utils import timezone
from datetime import datetime, timedelta


from celery.task.schedules import crontab
from celery.decorators import periodic_task

logger = get_task_logger(__name__)


@shared_task(name = "sleep_task")
def sleepy(duration):
	sleep(duration)
	return None


@shared_task(name='send_email_every_month_task')
def send_email_every_month_task():
	"""
	Function to send emails to the subscribers realated to their specific task once in a week
	"""

 # Get all tasks within month
	days_30=(timezone.now() - timedelta(days=30))
	# date_filtered=Task.objects.filter(created__gte=days_30).all()
	for i in range(1, 5):
		date_filtered = Task.objects.filter(created__gte = days_30).filter(task_type = i).all()
		tasks_json_objects = core_serializers.serialize('json', list(date_filtered), fields=("task_type", "task_desc"))
		json_tasks = json.loads(tasks_json_objects)

		email_list=[]
		tracker_objects = Task_tracker.objects.filter(update_type = "weekly").filter(task_type = i).all()
		tracker_objects_json = core_serializers.serialize('json', list(tracker_objects), fields=("email"))
		tracker_objects_list = json.loads(tracker_objects_json)

		for i in tracker_objects_list:
			for key, val in i.items():
				if key == "fields":
					email_list.append(i[key]['email'])

		tasks_message = ""

		for obj in json_tasks:
			for key, val in obj.items():
				if key == "fields":
					for t, d in obj[key].items():
						tasks_message=tasks_message+"  "+str(obj[key][t])

		# send mail requires 4 parameters "heading", "message body", "from", "to list"				
	
		logger.info("sending emails to type {} subscribers".format(i))
		send_mail("Updated Tasks", 
			"Message for updated tasks {}".format(tasks_message), 
			"revuriguna@gmail.com",
			email_list
			)
		return None

# @periodic_task(
#     run_every=(crontab(minute='*/1')),
#     name="send_email_every_day_task",
#     ignore_result=True
# )
@shared_task(name='send_email_every_day_task')
def send_email_every_day_task():
	"""
	Function to send emails to all subscribers related to their tasks in a day
	"""

 # Get all tasks within day
	days_diff=(timezone.now() - timedelta(days=1))
	# date_filtered=Task.objects.filter(created__gte=days_30).all()
	for i in range(1, 5):
		date_filtered = Task.objects.filter(created__gte = days_diff).filter(task_type = i).all()
		tasks_json_objects = core_serializers.serialize('json', list(date_filtered), fields=("task_type", "task_desc"))
		json_tasks = json.loads(tasks_json_objects)

		email_list=[]
		tracker_objects = Task_tracker.objects.filter(update_type = "Per Day").filter(task_type = i).all()
		tracker_objects_json = core_serializers.serialize('json', list(tracker_objects), fields=("email"))
		tracker_objects_list = json.loads(tracker_objects_json)

		for i in tracker_objects_list:
			for key, val in i.items():
				if key == "fields":
					email_list.append(i[key]['email'])

		print(email_list)


		tasks_message = ""

		for obj in json_tasks:
			for key, val in obj.items():
				if key == "fields":
					for t, d in obj[key].items():
						tasks_message=tasks_message+"  "+str(obj[key][t])
	
		logger.info("sending emails to type {} subscribers".format(i))

		# send mail requires 4 parameters "heading", "message body", "from", "to list"
		send_mail("Updated Tasks", 
			"Message for updated tasks {}".format(tasks_message), 
			"revuriguna@gmail.com",
			email_list
			)
		return None

@shared_task
def send_email_every_week_task():
	"""
	Function to send emails to the subscribers realated to their specific task once in a week
	"""

 # Get all tasks within a week
	days_7=(timezone.now() - timedelta(days = 7))
	# date_filtered=Task.objects.filter(created__gte=days_30).all()
	for i in range(1, 5):
		date_filtered = Task.objects.filter(created__gte = days_7).filter(task_type = i).all()
		tasks_json_objects = core_serializers.serialize('json', list(date_filtered), fields=("task_type", "task_desc"))
		json_tasks = json.loads(tasks_json_objects)

		tasks_message = ""

		email_list=[]
		tracker_objects = Task_tracker.objects.filter(update_type = "weekly").filter(task_type = i).all()
		tracker_objects_json = core_serializers.serialize('json', list(tracker_objects), fields=("email"))
		tracker_objects_list = json.loads(tracker_objects_json)

		for i in tracker_objects_list:
			for key, val in i.items():
				if key == "fields":
					email_list.append(i[key]['email'])

		for obj in json_tasks:
			for key, val in obj.items():
				if key == "fields":
					for t, d in obj[key].items():
						tasks_message=tasks_message+"  "+str(obj[key][t])
	# send mail requires 4 parameters "heading", "message body", "from", "to list"
		logger.info("sending emails to type {} subscribers".format(i))
		send_mail("Updated Tasks", 
			"Message for updated tasks {}".format(tasks_message), 
			"revuriguna@gmail.com",
			email_list
			)
		return None



@shared_task(name="email_task")
def send_email_task():
	logger.info("Sent Email")
	send_mail("Celery Task Worked sending mail", 
		"Message from clery task", 
		"revuriguna@gmail.com",
		 ['gunarevuri@gmail.com'])


	return None
# @shared_task(name="send_tasks")
# def send_tasks(tasks_json_list, email_list):
# 	logger.info("sending emails")
# 	send_mail("Updated Tasks", 
# 		"Message for updated tasks {}".format(tasks_json_list), 
# 		"revuriguna@gmail.com",
# 		email_list
# 		)
# 	return None



