import json, time, os
import csv
from django.shortcuts import render
from django.db.models import Max
# from models import Question, Option, Trigger, Group, Activity, Criterion


def home(request):
    return render(request, 'home.html', {})