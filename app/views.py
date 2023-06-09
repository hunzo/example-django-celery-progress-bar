from django.shortcuts import render, redirect
# from django.http import JsonResponse
from .tasks import Counter
from core.celery import app
from celery.utils.nodenames import gethostname
from pprint import pprint

# Create your views here.

def GetAllTasks():
    i = app.control.inspect().active()

    hostname = f"celery@{gethostname()}"

    tasks = []
    for t in i[hostname]:
        tasks.append(t['id'])
    return tasks
    
 
def Home(request):

    if request.method == "POST":
        Counter.delay(50)
        return redirect("home")   
    
    context = {
        "tasks": GetAllTasks()
    }

    return render(request, "index.html", context)

def CancelTask(request, task_id):
    task = Counter.AsyncResult(task_id).revoke(terminate=True)
    print(task) 
    return redirect('home')