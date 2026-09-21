from queue import Queue
import threading

workers = 4

job_queue = Queue()

def process_job(job):
    print("processed job", job)

def producer(job):
    job_queue.put(job)

def worker():
    while True:
        job = job_queue.get()
        process_job(job)
        job_queue.task_done()

for _ in range(workers):
    thread = threading.Thread(target=worker)
    thread.start()

for i in range(5):
    producer(i)
job_queue.join()

