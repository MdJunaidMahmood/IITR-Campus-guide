import datetime
from django.shortcuts import render
from django import forms

from .models import message
# Create your views here.
class NewSearchForm(forms.Form):
    search = forms.CharField(label="Search For Specific Organiser");

def index(request):
   currentDate = datetime.datetime.now()
   return render(request, "NoticeBoard/index.html", {
       "notice":message.objects.all().order_by('year', 'month', 'day'),
       "day":currentDate.day,
       "month":currentDate.month,
       "year":currentDate.year,
       "form" : NewSearchForm()
    })


def past(request):
   currentDate = datetime.datetime.now()
   return render(request, "NoticeBoard/past.html", {
       "notice":message.objects.all().order_by('-year', '-month', '-day'),
       "day":currentDate.day,
       "month":currentDate.month,
       "year":currentDate.year,
       "form" : NewSearchForm()
    })


def future(request):
   currentDate = datetime.datetime.now()
   return render(request, "NoticeBoard/future.html", {
       "notice":message.objects.all().order_by('year', 'month', 'day'),
       "day":currentDate.day,
       "month":currentDate.month,
       "year":currentDate.year,
       "form" : NewSearchForm()
    })

