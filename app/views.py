from django.shortcuts import render
from django.http import JsonResponse
from .tasks import Counter

# Create your views here.

def Home(request):
    ret = Counter.delay(50)
    print(ret)

    context = {
        "task_id": ret.task_id
    }
    return render(request, "index.html", context)

    # context = {
    #     "task_id": ret.task_id,
    #     "url": f"http://localhost:8000/celery-progress/{ret.task_id}"

    # }

    # return JsonResponse(context)
