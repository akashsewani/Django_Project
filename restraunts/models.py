from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


# Create your models here.
class RestrauntInfo(models.Model):
	Name=models.CharField(max_length=120)
	slug=models.SlugField(null=True, blank=True)
	Location=models.CharField(max_length=120, blank=True, default="Unknown")
	Category=models.CharField(max_length=120, null=True, blank=True)
	CreatedTime=models.DateTimeField(auto_now_add=False, default=timezone.now)
	UpdatedTime=models.DateTimeField(auto_now=False, default=timezone.now)
	
	
	#date3=models.DateTimeField(auto_now_add=True)
	#date1=models.DateTimeField(auto_now=True)

	#def __str__(self) :
	#	return  self.Name+" ,  "+ self.Location+" ,  "+ self.Category

			   
			   
	def next(self):
		return self.next()
		
	
	''' auto now add is used for timesatmp of adding time
		auto now is for current update timestamp
		marking true: we cannot make changes in admin mode
		marking false can make changes in admin mode'''
		
def ri_pre_save_reciever(sender, instance, *args, **kwargs):
		print('saving........')
		if not instance.slug:
			#instance.Name='Akash'
			instance.slug=unique_slug_generator(instance)
			instance.save()
		
		
#def ri_post_save_reciever(sender, instance,created, *args, **kwargs):
#		print('saved')
#		print(instance.UpdatedTime)
		
		
pre_save.connect(ri_pre_save_reciever, sender=RestrauntInfo, weak=False)
#post_save.connect(ri_post_save_reciever, sender=RestrauntInfo, weak=False)