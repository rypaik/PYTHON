import time
import threading
from memory_profiler import profile

def cpu_bound_job(job_id, num):
    start_job = time.time()    
    print(f"CPU-bound sub-job {job_id} started.")
    sum = 0
    # Simulated CPU-heavy arithmetic calculation.
    for i in range(num):
        sum += i
    duration = time.time() - start_job
    print(f"CPU-bound sub-job {job_id} finished in {duration:.2f} seconds.")

@profile
def run_with_threads(n_jobs, num):
    threads = []
    for _id in range(n_jobs):
        # `args` is a tuple specifying the positional arguments for the
        # target function, which will be run in an independent thread.
        thread = threading.Thread(target=cpu_bound_job, args=(_id, num))
        threads.append(thread)
        thread.start()

    for thread in threads:
        # With `oin`, we wait until the thread terminates, either normally
        # or through an unhandled exception.
        thread.join()

start_one_thread = time.time()
# Run with a single thread, with a big number.
run_with_threads(n_jobs=1, num=3*10**8)
duration = time.time() - start_one_thread
print(f"CPU-bound job finished in {duration:.2f} seconds with a single thread.")

start_three_threads = time.time()
# Run with three threads with a smaller number. The total number of three threads
# adds up to the one of a single thread so the result is comparable.
run_with_threads(n_jobs=3, num=10**8)
duration = time.time() - start_three_threads
print(f"CPU-bound job finished in {duration:.2f} seconds with three threads.")

# CPU-bound sub-job 0 started.
# CPU-bound sub-job 0 finished in 15.14 seconds.
# CPU-bound job finished in 15.14 seconds with a single thread.
# CPU-bound sub-job 0 started.
# CPU-bound sub-job 1 started.
# CPU-bound sub-job 2 started.
# CPU-bound sub-job 0 finished in 18.40 seconds.
# CPU-bound sub-job 2 finished in 18.62 seconds.
# CPU-bound sub-job 1 finished in 19.13 seconds.
# CPU-bound job finished in 19.13 seconds with three threads.

