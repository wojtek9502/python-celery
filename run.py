from celery_app.tasks import add

add.delay(2,2)