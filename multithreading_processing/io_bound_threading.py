import time
import threading

def io_bound_job(job_id, num_requests):
    start_job = time.time()
    print(f"IO-bound sub-job {job_id} started.")
    for _ in range(num_requests):
        # IO-bound jobs spend most of the time waiting for responses.
        time.sleep(3)
    duration = time.time() - start_job
    print(f"IO-bound sub-job {job_id} finished in {duration:.2f} seconds.")

def run_with_threads(n_jobs, num_requests_per_job):
    threads = []
    for _id in range(n_jobs):
        thread = threading.Thread(target=io_bound_job, args=(_id, num_requests_per_job))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

start_one_thread = time.time()
# Run with a single thread:
run_with_threads(n_jobs=1, num_requests_per_job=3)
duration = time.time() - start_one_thread
print(f"IO-bound job finished in {duration:.2f} seconds with a single thread.")

start_three_threads = time.time()
# Run with three threads:
run_with_threads(n_jobs=3, num_requests_per_job=1)
duration = time.time() - start_three_threads
print(f"IO-bound job finished in {duration:.2f} seconds with three threads.")

# IO-bound sub-job 0 started.
# IO-bound sub-job 0 finished in 9.01 seconds.
# IO-bound job finished in 9.01 seconds with a single thread.
# IO-bound sub-job 0 started.
# IO-bound sub-job 1 started.
# IO-bound sub-job 2 started.
# IO-bound sub-job 0 finished in 3.00 seconds.
# IO-bound sub-job 1 finished in 3.00 seconds.
# IO-bound sub-job 2 finished in 3.00 seconds.
# IO-bound job finished in 3.00 seconds with three threads.

