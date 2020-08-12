from django.db import models

update_type_list = ["Per Day", "weekly", "monthly"]
weekly_list = ["mon", "tue", "wed", "thu","fri","sat","sun"]


class Task(models.Model):
	task_type   = models.IntegerField(verbose_name="Type Of Task " , choices=[(x,x) for x in range(1,5)], null=False, blank=False )
	task_desc   = models.CharField(verbose_name="Task Description", max_length=500)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.task_type}"
class Task_tracker(models.Model):
	task_type   = models.IntegerField(verbose_name="Type of Task to track", choices=[(x,x) for x in range(1,5)], null=False,blank=False)
	update_type = models.CharField(verbose_name="Task Update Type", max_length=20 , choices=[(x,x) for x in update_type_list], null=False, blank=False)
	email       = models.EmailField(verbose_name='Email')
	def __str__(self):
		return f"{self.task_type} {self.email}"

class Update_type(models.Model):
	Weekly      = models.CharField(verbose_name='Day of week to update', max_length=100 ,choices=[(x,x) for x in weekly_list], null=True, blank=True)
	daily       = models.IntegerField(verbose_name="Time in day to update(Hour)", choices=[(x,x) for x in range(1, 25)], null=True,  blank=True)
	monthly     = models.IntegerField(verbose_name="Month In year to update", choices=[(x,x) for x in range(1, 13)], null=True, blank=True)





