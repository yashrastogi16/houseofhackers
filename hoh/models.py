from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone
from datetime import datetime

# class contestant_info(models.Model):
# 	university = models.CharField('University', max_length=60)
# 	username = models.CharField('Name',max_length=60)
# 	dob = models.CharField('Date Of Birth', max_length=60)
# 	location = models.CharField('Location', max_length=60)
# 	email_id = models.EmailField('Email', max_length=60)
# 	self_description = models.TextField()
# 	achievements = models.TextField()
# 	project_name = models.CharField('Project Name', max_length=60)
# 	project_link = models.URLField('Project Link', max_length=255)
# 	project_Description = models.TextField()
# 	skills_used = models.TextField()
# 	date_time = models.DateTimeField(auto_now=True)
# 	def __unicode__(self):
# 		return smart_unicode(self.email_id)


class contestant_info(models.Model):
	university = models.CharField('University', max_length=60)
	username = models.CharField('Name',max_length=60)
	link_stockroom = models.CharField('Link_Stockroom', max_length=255)
	location = models.CharField('Location', max_length=60)
	email_id = models.EmailField('Email', max_length=60)
	self_description = models.TextField()
	achievements = models.TextField()
	project = models.TextField()
	date_time = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.email_id)

class feedback(models.Model):
	Name = models.CharField('Name', max_length=60)
	email_id = models.EmailField('Email', max_length=255)
	query = models.TextField()
	def __unicode__(self):
		return smart_unicoode(self.email_id)