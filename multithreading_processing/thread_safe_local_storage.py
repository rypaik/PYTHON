import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# `threading.local()`, similar to `globals()`, but returns variables that
# are only accessible to a thread.
thread_local = threading.local()

def get_session():
    # Get a session object for each thread.
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session  

def io_bound_job(site):
    session = get_session()
    resp = session.get(site)
    print(f"Response status of {site} is {resp.status_code}.")

def run_with_threads(n_jobs, sites):
    # `max_workers` specifies the max number threads to created.
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        # When the taget function is mapped to a list or tuple, the target function
        # is executed for every element of the list or tuple in a separate thread.
        executor.map(io_bound_job, sites)

# Get a list of fake websites for testing.
sites = [f"https://httpbin.org/get?id={i}" for i in range(20)]

# Run with one thread:
start_one_thread = time.time()
run_with_threads(n_jobs=1, sites=sites)
duration = time.time() - start_one_thread
print(f"IO-bound job finished in {duration:.2f} seconds with one thread.")
                        
# Run with ten threads:
start_three_threads = time.time()
run_with_threads(n_jobs=10, sites=sites)
duration = time.time() - start_three_threads
print(f"IO-bound job finished in {duration:.2f} seconds with three threads.")

# Response status of https://httpbin.org/get?id=0 is 200.
# Response status of https://httpbin.org/get?id=1 is 200.
# Response status of https://httpbin.org/get?id=2 is 200.
# ......
# Response status of https://httpbin.org/get?id=18 is 200.
# Response status of https://httpbin.org/get?id=19 is 200.
# IO-bound job finished in 4.43 seconds with one thread.

# Response status of https://httpbin.org/get?id=0 is 200.
# Response status of https://httpbin.org/get?id=2 is 200.
# Response status of https://httpbin.org/get?id=3 is 200.
# ......
# Response status of https://httpbin.org/get?id=18 is 200.
# Response status of https://httpbin.org/get?id=19 is 200.
# IO-bound job finished in 0.63 seconds with three threads.r
