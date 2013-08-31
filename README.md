What's this lib?
================

This project is a Python library to connect and manage the latest OpenVAS servers using the OMPv4 protocol.

Why this lib?
=============

There is an [official python library](https://pypi.python.org/pypi/openvas.omplib) for OpenVAS, but it doesn't work with OMPv4 based versions (OpenVAS 6).

Quick start
===========

Downloading
-----------

To download the latest source code enter the following command:

```git clone https://github.com/cr0hn/OpenVas.git openvas_lib```

Usage
-----

Connect to the server
_____________________


```
from openvas_lib import VulnscanManager, VulnscanException

try:
	scanner = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
except VulnscanException, e:
	print "Error:"
	print e
```

Launch a simple scan
____________________

```
from openvas_lib import VulnscanManager, VulnscanException

scanner            = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
scan_id, target_id = scanner.launch_scan(
                target = "127.0.0.1", # Target to scan
                profile = "Full and fast")
```            

Launch advanced scan
____________________

The library supports callbacks. They will be run every 10 seconds and report the status of the scan ("callback_progress") or the end of the scan ("callback_end").

```
from openvas_lib import VulnscanManager, VulnscanException
from threading import Semaphore
from functools import partial

def my_print_status(i): print str(i)

def my_launch_scanner():

    Sem = Semaphore(0)

    # Configure
    manager = VulnscanManager.connectOpenVAS("localhost", "admin", "admin)

    # Launch
    manager.launch_scan(
        target,
        profile = "empty",
        callback_end = partial(lambda x: x.release(), sem),
        callback_progress = my_print_status
    )

    # Wait
    Sem.acquire()

    # Finished scan
    print "finished!"

# my_launch_scanner() # It can take some time
# 0
# 10
# 39
# 60
# 90
# finished!
```

Get results of scan
___________________

```
from openvas_lib import VulnscanManager, VulnscanException

scanner         = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
openvas_results = scanner.get_results(SCAN_ID)
```

Delete scan
___________

```
from openvas_lib import VulnscanManager, VulnscanException

scanner         = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
scanner.delete_scan(SCAN_ID)
```

Delete target
_____________

```
from openvas_lib import VulnscanManager, VulnscanException

scanner         = VulnscanManager(HOST, USER, PASSWORD, PORT, TIMEOUT)
scanner.delete_target(TARGET_ID)
```


