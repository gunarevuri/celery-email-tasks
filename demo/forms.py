from django import forms

class TaskForm(forms.Form):
	task_type = forms.IntegerField(label="Task type")
	task_desc = forms.CharField(label="Task Description")



class TaskTrackerForm(forms.Form):
	task_type = forms.IntegerField(label="Task type")
	update_type = forms.CharField(label="Update Type")
	email = forms.EmailField(label="Email")

class UpdateTypeForma(forms.Form):
	daily = forms.IntegerField(label="Update Daily")
	weekly = forms.CharField(label="Update weekly")
	monthly  = forms.IntegerField(label="update monthly")

	