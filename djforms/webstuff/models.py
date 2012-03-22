from django.db import models

# Create your models here.
# Marcos Lopez - dev@scidentify.info

class Teachers(models.Model):
	""" Teachers """
	def __str__(self):
		return str(self.name)
	def __unicode__(self.name):
		return unicode(self.name)
	def get_students(self):
		return self.student_set.select_related()
	fname = models.CharField(max_length=30, verbose_name=('First Name'))
	lname = models.CharField(max_length=30, verbose_name=('Last Name'))

class Student(models.Model):
	""" STudent belonds to a teacher """
	def __str__(self):
		return str(self.name)
	def __unicode__(self.name):
		return unicode(self.name)
	fname = models.CharField(max_length=30, verbose_name=('First Name'))
	lname = models.CharField(max_length=30, verbose_name=('Last Name'))
	teacher = models.ForeignKey('Teachers')

