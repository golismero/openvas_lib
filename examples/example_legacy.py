#!/usr/bin/env python

from __future__ import print_function

from openvas_lib import VulnscanManager, VulnscanException
from threading import Semaphore
from functools import partial
from xml.etree import ElementTree
import base64
import os,sys
import argparse

def my_print_status(i):
	print(str(i)),
	sys.stdout.flush()

def write_report(manager, report_id, ip):
	result_dir = os.path.dirname(os.path.abspath(__file__)) + "/results"
	if not os.path.exists(result_dir):
		os.makedirs(result_dir)

	try:
		report = manager.get_report_xml(report_id)
	except Exception as e:
		print(e)
		return
	else:
		fout_path = result_dir + "/xml/"
		if not os.path.exists(fout_path):
			os.makedirs(fout_path)
		
		fout = open(fout_path + ip + ".xml", "wb")
		fout.write(ElementTree.tostring(report, encoding='utf-8', method='xml'))
		fout.close()

	try:
		report = manager.get_report_html(report_id)
	except Exception as e:
		print(e)
		return
	else:
		fout_path = result_dir + "/html/"
		if not os.path.exists(fout_path):
			os.makedirs(fout_path)

		html_text = report.find("report").text
		if not html_text:
			html_text = report.find("report").find("report_format").tail

		fout = open(fout_path + ip + ".html", "wb")
		fout.write(base64.b64decode(html_text))
		fout.close()

def run(manager, ip):
	Sem = Semaphore(0)
	scan_id, target_id = manager.launch_scan(
		target=ip,
		profile="Full and fast",
		callback_end=partial(lambda x: x.release(), Sem),
		callback_progress=my_print_status
	)
	Sem.acquire()
	report_id = manager.get_report_id(scan_id)

	write_report(manager, report_id, ip)
	manager.delete_scan(scan_id)
	manager.delete_target(target_id)

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Features Selection')
	parser.add_argument('-u', '--user', required=True, help='OpenVas user')
	parser.add_argument('-p', '--password', required=True, help='OpenVas password')
	parser.add_argument('-i', '--ip', required=True, help='OpenVas ip host')
	parser.add_argument('-t', '--target', required=True, help='Host target')

	args = parser.parse_args()

	if args.user:
		admin_name = args.user
	if args.user:
		admin_password = args.password
	if args.ip:
		openvas_ip = args.ip
	if args.target:
		ip = args.target

	try:
		manager = VulnscanManager(openvas_ip, admin_name, admin_password)
		run(manager, ip)
	except Exception as e:
		print(e)
