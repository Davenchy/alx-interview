#!/usr/bin/python3
import random
import sys
import os
from time import sleep
import datetime

log_temp = "{:d}.{:d}.{:d}.{:d} - [{}] "
log_temp += '"GET /projects/260 HTTP/1.1"'
log_temp += " {} {}\n"


iterations = int(sys.argv[1]) if len(sys.argv) >= 2 else 10000
for i in range(iterations):
    sleep(random.random())
    sys.stdout.write(log_temp.format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
