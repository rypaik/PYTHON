import re
from time import sleep
from timeit import timeit

# Simple demo
from tqdm import trange

for _ in trange(16, leave=True):
    sleep(0.1)

# Profiling/overhead tests
#BUG: filter expected str
stmts = filter(None, re.split(r'\n\s*#.*?\n', __doc__))
for s in stmts:
    print(s.replace('import tqdm\n', ''))
    print(timeit(stmt='try:\n\t_range = xrange'
                 '\nexcept:\n\t_range = range\n' + s, number=1), 'seconds')
