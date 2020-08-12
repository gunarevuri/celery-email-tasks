from celery import Celery
import os
from celery.schedules import crontab
from demo.tasks import send_email_every_day_task, send_email_every_month_task, send_email_every_week_task

# Setting the Default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery_trail.settings')
app=Celery('celery_trail', backend='redis', broker='redis://localhost:6379')


# Using a String here means the worker will always find the configuration information
app.config_from_object('django.conf:settings')



app.conf.beat_schedule = {
	'send_email_every_day_task':{
	'task': 'demo.tasks.send_email_every_day_task',
	# task to send emails at 1:30 AM every data
	'schedule': crontab(minute = '30', hour = '1',day_of_month = '*',month_of_year = '*'),
	},
	'send_email_every_month_task': {
	'task': 'demo.tasks.send_email_every_month_task',
	# task to send emails at 1:30 AM every first day in month
	'schedule': crontab( minute = '30' , hour = '1', day_of_month = '1')
	},
	'send_email_every_week_task' :{
	# task to send emails at 1:30Am every first week of month
	'task': 'demo.tasks.send_email_every_week_task',
	'schedule': crontab( minute = '30', hour = '1', day_of_week = '1')
	}
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

