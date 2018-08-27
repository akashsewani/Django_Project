from django.db import models
from django.utils import timezone

# Create your models here.
class RestrauntInfo (models.Model):
	Name=models.CharField(max_length=120)
	Location=models.CharField(max_length=120, blank=True, default="Unknown")
	Category=models.CharField(max_length=120, null=True, blank=True)
	CreatedTime=models.DateTimeField(auto_now_add=False, default=timezone.now)
	UpdatedTime=models.DateTimeField(auto_now=False, default=timezone.now)
	
	#date3=models.DateTimeField(auto_now_add=True)
	#date1=models.DateTimeField(auto_now=True)

	#def __str__(self) :
	#	return  self.Name+" ,  "+ self.Location+" ,  "+ self.Category
	
	def __iter__(self):
		return ([
				self.Name,
				self.Location,
				self.Category,
				self.CreatedTime,
				self.UpdatedTime
			   ])
	def next(self):
		return self.next()
		
	
	''' auto now add is used for timesatmp of adding time
		auto now is for current update timestamp
		marking true: we cannot make changes in admin mode
		marking false can make changes in admin mode'''