broker_url = 'amqp://pi:pi@localhost:5672//'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Warsaw'
enable_utc = True
result_expires = 3600