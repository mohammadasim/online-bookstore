from celery import shared_task


@shared_task
def print_greetings(numb, review_type):
    for no in range(numb):
        print('A {} review was submitted.'.format(review_type))
