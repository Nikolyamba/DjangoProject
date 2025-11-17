from celery import shared_task

@shared_task
def sum_numbers(numbers):
    return sum(numbers)

@shared_task
def reverse_text(text):
    return text[::-1]

@shared_task
def delayed(seconds):
    import time
    time.sleep(seconds)
    return f"Waited {seconds} seconds"