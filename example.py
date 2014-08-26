##!/usr/bin/env python
from openvas_lib import VulnscanManager,VulnscanException
from threading import Semaphore
from functools import partial
from xml.etree import ElementTree
import base64
import datetime
import os
import sys,re
import subprocess

manager= VulnscanManager("127.0.0.1","admin","******")
totalscan=0
totalread=0
def my_print_status(i):
    print str(i),
    sys.stdout.flush()
def runCheck(host):
    p=subprocess.Popen(["ping -c 1 "+host], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out=p.stdout.read()
    regex = re.compile("time=\d*", re.IGNORECASE | re.MULTILINE)
    if len(regex.findall(out)) > 0:
         return True
    else:
         return False
def write_report(report_id,myip,myemail):
    global manager
    global totalscan 
    Mydir="/root/myopenvas/results/"+myemail[0:myemail.find('@')]
    if not os.path.exists(Mydir):
        os.mkdir(Mydir)
    fout=open(Mydir+"/"+myip+".html","wb")
    report=manager.get_report_html(report_id)
    fout.write(base64.b64decode(report.find("report").text))
    fout.close()

    fout=open(Mydir+"/"+myip+".pdf","wb")
    report=manager.get_report_pdf(report_id)
    fout.write(base64.b64decode(report.find("report").text))
    fout.close()
    totalscan+=1
    print "have scan : ",totalscan

#    fout=open(Mydir+"/"+myip+".xml","w")
#    report=manager.get_report(report_id)
#    fout.write(ElementTree.tostring(report,encoding='utf-8',method='xml'))
#    fout.close()

def my_scan(myip,myemail):
    global manager
    Mydir="/root/myopenvas/results/"+myemail[0:myemail.find('@')]
    if os.path.isfile(Mydir+"/"+myip+".html"):
        print myip+" already exist"
        return 
    start=datetime.datetime.now()
    print "Start of: "+myip+" at : ",start
#    """
    Sem =Semaphore(0)
    scan_id,target_id=manager.launch_scan(
            target=myip,
            profile="Full and fast",
            callback_end=partial(lambda x:x.release(),Sem),
            callback_progress=my_print_status
            )
    Sem.acquire()
#    """
    end=datetime.datetime.now()
    print "End of: "+myip+" at : ",end
    print "*******************************"
    print "Cost :",(end-start)
    print "*******************************"

    report_id=manager.get_tasks_last_report_id(scan_id)
    write_report(report_id,myip,myemail)
def my_launch_scanner():
    global totalread
    fp=open("last.txt","r")
    lines =fp.readlines()
    for line in lines:
        line=line.split(' ')
        totalread+=1
        print "have read : ",totalread
        print "========================================================================"
        if runCheck(line[0]):
            try:
                my_scan(line[0],line[1])
            except:
                print "my error found"
                return 
        print "========================================================================"
my_launch_scanner()
