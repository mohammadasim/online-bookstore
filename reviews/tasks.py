from celery import shared_task


@shared_task
def print_greetings(numb):
    for no in range(numb):
        print('Running first celery task.')
