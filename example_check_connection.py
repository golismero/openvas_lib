# -*- coding: utf-8 -*-

from __future__ import print_function

from functools import partial
from threading import Semaphore

from openvas_lib import VulnscanManager, VulnscanException


def my_print_status(i):
	print(str(i))


def my_launch_scanner():
	sem = Semaphore(0)

	# Configure
	manager = VulnscanManager("localhost", "admin", "openvas")

	# Launch
	manager.launch_scan("127.0.0.1",
	                    profile="empty",
	                    callback_end=partial(lambda x: x.release(), sem),
	                    callback_progress=my_print_status)

	# Wait
	sem.acquire()

	# Finished scan
	print("finished")


if __name__ == '__main__':
	my_launch_scanner()

