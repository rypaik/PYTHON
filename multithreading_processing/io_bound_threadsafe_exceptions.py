import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

thread_local = threading.local()

def get_session():
    # Get a different session for each thread.
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session  

def io_bound_job(site):
    session = get_session()
    # `timeout` is so small that a `ConnectTimeoutError` exception will be raised here.
    resp = session.get(site, timeout=0.001)
    print(f"Response status of {site} is {resp.status_code}.")

def run_with_threads(n_jobs, sites):
    futures = []
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        for site in sites:
            # The `submit` methd returns a `future`, which is an object representing
            # the execution of the target function run in a thread.
            future = executor.submit(io_bound_job, site)
            futures.append(future)
    
    # `as_completed` returns the futures that are completed or cancelled.
    futures_completed = as_completed(futures)    
    try:
        for future in futures_completed:
            # `result()` returns the result of the function that the future represents
            future.result()
    except Exception as exc:
        # If there is an exception raised in any thread, it will be caught here.
        print(f"An error occured in a thread: {exc}")

sites = [f"https://httpbin.org/get?id={i}" for i in range(20)]

# Run with one thread:
start_one_thread = time.time()
run_with_threads(n_jobs=1, sites=sites)
duration = time.time() - start_one_thread
print(f"IO-bound job finished in {duration:.2f} seconds with one thread.")
                        
# Run with three threads:
start_three_threads = time.time()
run_with_threads(n_jobs=10, sites=sites)
duration = time.time() - start_three_threads
print(f"IO-bound job finished in {duration:.2f} seconds with three threads.")

# An error occured in a thread: ...... 'Connection to httpbin.org timed out. (connect timeout=0.001)'))
# IO-bound job finished in 0.43 seconds with one thread.
# An error occured in a thread: ...... 'Connection to httpbin.org timed out. (connect timeout=0.001)'))
# IO-bound job finished in 0.09 seconds with three threads.o
