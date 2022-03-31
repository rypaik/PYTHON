import queue
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

thread_local = threading.local()

def get_session():
    # Get a different session for each thread, because `Session` is not thread-safe.
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session  

def publisher(result_queue, site):
    session = get_session()
    resp = session.get(site)
    result = {"site": site, "status": resp.status_code, "args": resp.json()["args"]}
    # Publish a result to the queue.
    result_queue.put(result)

def subscriber(result_queue, event):
    # Keep checking for new messages until the terminal signal is sent or
    # when the queue is empty.
    while not event.is_set() or not result_queue.empty():
        try:
            # Set timeout in case no messages will ever be sent.
            # Otherwise, the subscriber will get blocked here.
            result = result_queue.get(timeout=1)
            print(f"Get result: {result}")    
        except queue.Empty:
            # No result yet, keep waiting.
            continue
    
def run_with_threads(n_jobs, sites):
    # Set a max size for the Queue, if the number of messages in the
    # queue exceeds the max size, the publisher will be blocked and
    # cannot send new messages to the queue.
    result_queue = queue.Queue(maxsize=n_jobs)
    # `event` is used to send a terminating signal to the subscriber so
    # it will keep waiting until all the messages have been received.
    event = threading.Event()
    _futures = []
    
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        # The subscriber can be started before the the publisher. It will
        # keep waiting until the terminating signal is sent or the queue
        # is empty.
        future_sub = executor.submit(subscriber, result_queue, event)
        _futures.append(future_sub)
        for site in sites:
            future_pub = executor.submit(publisher, result_queue, site)
            _futures.append(future_pub)
        
        # Sleep for a short period before the terminating signal is sent.
        # In this way, there can be enough time for the first messages to
        # be sent so the subscriber won't exit immediately.
        time.sleep(2)
        event.set()
    
    futures_completed = as_completed(_futures)    
    try:
        for future in futures_completed:
            future.result()
    except Exception as exc:
        print(f"An error occured in a thread: {exc}")

sites = [f"https://httpbin.org/get?id={i}" for i in range(20)]
                        
run_with_threads(n_jobs=10, sites=sites)

# Get result: {'site': 'https://httpbin.org/get?id=7', 'status': 200, 'args': {'id': '7'}}
# Get result: {'site': 'https://httpbin.org/get?id=9', 'status': 200, 'args': {'id': '9'}}
# Get result: {'site': 'https://httpbin.org/get?id=10', 'status': 200, 'args': {'id': '10'}}
# ......
# Get result: {'site': 'https://httpbin.org/get?id=6', 'status': 200, 'args': {'id': '6'}}
# Get result: {'site': 'https://httpbin.org/get?id=1', 'status': 200, 'args': {'id': '1'}}
# Get result: {'site': 'https://httpbin.org/get?id=0', 'status': 200, 'args': {'id': '0'}}
