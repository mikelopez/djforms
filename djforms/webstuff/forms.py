from django import forms

from django.contrib.auth.models import User, Group
from django.forms.util import ErrorList
from django.forms import ModelForm
from datetime import date, timedelta, datetime

from models import *
from random import randint, getrandbits
from settings import MEDIA_ROOT

# forms example - Marcos Lopez - dev@scidentify.info

class TeachersForm(ModelForm):
  class Meta:
    model = Teachers
  
  def clean(self):
    # clean data
    return self.cleaned_data

  def clean_fname(self):
    # clean the first name field
    return self.cleaned_data

  def save(self):
    # do stuff before saving
    pass

  def update(self, id):
    for k,v in self.cleaned_data.items():
      setattr(pl, k, v)


class StudentForm(ModelForm):
  class Meta:
    model = Student
  
  def clean(self):
    # clean data
    return self.cleaned_data

  def clean_fname(self):
    # clean the first name field
    return self.cleaned_data

  def save(self):
    # do stuff before saving
    pass

  def update(self, id):
    for k,v in self.cleaned_data.items():
      setattr(pl, k, v)

