# !/usr/bin/env python

import os
import re
import sys
import base64
import datetime
import subprocess
from functools import partial
from threading import Semaphore
from xml.etree import ElementTree

from openvas_lib import VulnscanManager

manager = VulnscanManager("127.0.0.1", "admin", "******")
total_scan = 0
total_read = 0


def my_print_status(i):
    print str(i),
    sys.stdout.flush()


def run_check(host):
    p = subprocess.Popen(["ping -c 1 " + host], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out = p.stdout.read()
    regex = re.compile("time=\d*", re.IGNORECASE | re.MULTILINE)
    if len(regex.findall(out)) > 0:
        return True
    else:
        return False


def write_report(report_id, my_ip, my_email):
    global manager
    global total_scan

    my_dir = "/root/myopenvas/results/" + my_email[0:my_email.find('@')]

    if not os.path.exists(my_dir):
        os.mkdir(my_dir)

    f_out = open(my_dir + "/" + my_ip + ".html", "wb")
    report = manager.get_report_html(report_id)
    f_out.write(base64.b64decode(report.find("report").text))
    f_out.close()

    f_out = open(my_dir + "/" + my_ip + ".pdf", "wb")
    report = manager.get_report_pdf(report_id)
    f_out.write(base64.b64decode(report.find("report").text))
    f_out.close()
    total_scan += 1
    print "have scan : ", total_scan

#    fout=open(Mydir+"/"+myip+".xml","w")
#    report=manager.get_report(report_id)
#    fout.write(ElementTree.tostring(report,encoding='utf-8',method='xml'))
#    fout.close()


def my_scan(my_ip, my_email):
    global manager
    my_dir = "/root/myopenvas/results/" + my_email[0:my_email.find('@')]

    if os.path.isfile(my_dir + "/" + my_ip + ".html"):
        print my_ip + " already exist"
        return
    start = datetime.datetime.now()
    print "Start of: " + my_ip + " at : ", start
#    """
    sem = Semaphore(0)

    scan_id, target_id = manager.launch_scan(
        target=my_ip,
        profile="Full and fast",
        callback_end=partial(lambda x: x.release(), sem),
        callback_progress=my_print_status
    )
    sem.acquire()
#    """
    end = datetime.datetime.now()
    print "End of: " + my_ip + " at : ", end
    print "*******************************"
    print "Cost :", (end - start)
    print "*******************************"

    report_id = manager.get_tasks_last_report_id(scan_id)
    write_report(report_id, my_ip, my_email)


def my_launch_scanner():
    global total_read
    fp = open("last.txt", "r")
    lines = fp.readlines()
    for line in lines:
        line = line.split(' ')
        total_read += 1
        print "have read : ", total_read
        print "========================================================================"
        if run_check(line[0]):
            try:
                my_scan(line[0], line[1])
            except:
                print "my error found"
                return
        print "========================================================================"
my_launch_scanner()
