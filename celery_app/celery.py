from celery import Celery

app = Celery('celery_app', #module name with files withtasks
             include=['celery_app.tasks'])

app.config_from_object("celery_app.celeryconfig")