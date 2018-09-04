from celery import Celery

app = Celery('tasks', broker='redis://')

if __name__ == '__main__':
    app.start()
