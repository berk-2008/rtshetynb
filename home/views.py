from django.shortcuts import render
from .models import BLog
def index(reguest):
    blogs = BLog.objects.all()
    print(blogs)
    context = {
        'blogs':blogs
    }
    return render(reguest,"home/index.html", context)