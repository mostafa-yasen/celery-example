from celery import Celery
from time import sleep

REDIS_URL = "redis://127.0.0.1:6379"
TASKS_DB = "db+sqlite:///results.db"

app = Celery('tasks', broker=REDIS_URL, backend=TASKS_DB)

@app.task
def add(x: float, y: float) -> float:
  """Performs a simple add operation between to given float numbers after 5 seconds"""
  sleep(5)
  return x + y
