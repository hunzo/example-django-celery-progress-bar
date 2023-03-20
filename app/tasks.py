from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder

@shared_task(bind=True)
def Counter(self, counter):

    print(self.request.id)
    progress_recorder = ProgressRecorder(self)

    for i in range(counter):
        i += 1
        print(f'task_id: {self.request.id} count: {i}')
        sleep(0.3)
        progress_recorder.set_progress(i + 1, counter)
    
    return "done"