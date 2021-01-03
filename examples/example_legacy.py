# #!/usr/bin/env python


import base64
import os
import sys
import argparse

from openvas_lib import VulnscanManager, VulnscanException
from threading import Semaphore
from functools import partial
from xml.etree import ElementTree


def my_print_status(i):
	print(str(i)),
	sys.stdout.flush()


def write_report(_manager, report_id, ip):
	result_dir = os.path.dirname(os.path.abspath(__file__)) + "/results"
	if not os.path.exists(result_dir):
		os.makedirs(result_dir)

	try:
		report = _manager.get_report_xml(report_id)
	except Exception as e:
		print(str(e))
		return
	else:
		fout_path = result_dir + "/xml/"
		if not os.path.exists(fout_path):
			os.makedirs(fout_path)

		fout = open(fout_path + ip + ".xml", "wb")
		fout.write(ElementTree.tostring(report, encoding='utf-8', method='xml'))
		fout.close()

	try:
		report = _manager.get_report_html(report_id)
	except Exception as e:
		print(str(e))
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


def run(_manager, _target, _profile):
	sem = Semaphore(0)
	scan_id, target_id = _manager.launch_scan(
		target=_target,
		profile=_profile,
		callback_end=partial(lambda x: x.release(), sem),
		callback_progress=my_print_status
	)
	sem.acquire()
	report_id = _manager.get_report_id(scan_id)
	write_report(_manager, report_id, _target)
	_manager.delete_scan(scan_id)
	_manager.delete_target(target_id)


def main(ip, user, password, target, profile):
	try:
		manager = VulnscanManager(ip, user, password)
	except VulnscanException as e:
		print(str(e))
	else:
		run(manager, target, profile)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Features Selection')
	parser.add_argument('-u', '--user', required=True, help='OpenVas user')
	parser.add_argument('-p', '--password', required=True, help='OpenVas password')
	parser.add_argument('-i', '--ip', required=True, help='OpenVas ip host')
	parser.add_argument('-t', '--target', required=True, help='Host target')
	parser.add_argument('--profile', required=True, help='OpenVas profile, ex: --profile="Full and fast"')
	args = parser.parse_args()

	print(args.ip, args.user, args.password, args.target, args.profile)
