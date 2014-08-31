import unittest
import StringIO

try:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree

from openvas_lib import VulnscanManager, report_parser


class TestVulnscanManager(unittest.TestCase):

    # --------------------------------------------------------------------------
    # __init__
    # --------------------------------------------------------------------------
    def test___init__types(self):
        self.assertRaises(TypeError, VulnscanManager, 0, None, None, None, None)
        self.assertRaises(TypeError, VulnscanManager, "127.0.0.1", 0, None, None, None)
        self.assertRaises(TypeError, VulnscanManager, "127.0.0.1", "a", 0, None, None)
        self.assertRaises(TypeError, VulnscanManager, "127.0.0.1", "a", "b", "a")
        self.assertRaises(ValueError, VulnscanManager, "127.0.0.1", "a", "b", -1)
        self.assertRaises(TypeError, VulnscanManager, "127.0.0.1", "a", "b", 80, "a")
        self.assertRaises(ValueError, VulnscanManager, "127.0.0.1", "a", "b", 80, -1)

    # def test_delete_scan(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.delete_scan(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_delete_target(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.delete_target(target_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_all_scans(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_all_scans())
    #     assert False  # TODO: implement your test here
    #
    # def test_get_finished_scans(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_finished_scans())
    #     assert False  # TODO: implement your test here
    #
    # def test_get_profiles(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_profiles())
    #     assert False  # TODO: implement your test here
    #
    # def test_get_progress(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_progress(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_html(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_report_html(report_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_id(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_report_id(scan_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_pdf(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_report_pdf(report_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_xml(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_report_xml(report_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_results(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_results(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_running_scans(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.get_running_scans())
    #     assert False  # TODO: implement your test here
    #
    # def test_launch_scan(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.launch_scan(target, **kwargs))
    #     assert False  # TODO: implement your test here
    #
    # def test_stop_audit(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.stop_audit(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_target_id(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.target_id())
    #     assert False  # TODO: implement your test here
    #
    # def test_task_id(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.task_id())
    #     assert False  # TODO: implement your test here
    #
    # def test_transform(self):
    #     # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
    #     # self.assertEqual(expected, vulnscan_manager.transform(version))
    #     assert False  # TODO: implement your test here


# --------------------------------------------------------------------------
class TestReportParser(unittest.TestCase):

    def setUp(self):
        import os

        self.path = os.path.abspath("metasploitable_all.xml")

    # ----------------------------------------------------------------------
    def test_report_parser_types(self):
        self.assertRaises(TypeError, report_parser, 0)
        self.assertRaises(TypeError, report_parser, None)

    # ----------------------------------------------------------------------
    def test_report_parser_file_not_exits(self):
        self.assertRaises(IOError, report_parser, "asdfasf")

    # ----------------------------------------------------------------------
    def test_report_parser_is_not_file(self):
        self.assertRaises(IOError, report_parser, "./")

    # ----------------------------------------------------------------------
    def test_report_parser_invalid_xml_file(self):
        xml = StringIO.StringIO("<hellos><hello>asdf</hellos>")
        self.assertRaises(etree.ParseError, report_parser, xml)

    def test_report_parser_invalid_xml_without_id(self):
        xml = StringIO.StringIO('<report extension="xml" type="scan" content_type="text/xml" format_id="a994b278-1f62-11e1-96ac-406186ea4fc5"><hello></hello></report>')

        self.assertRaises(ValueError, report_parser, xml)

    def test_report_parser_check_empty_results(self):
        xml = StringIO.StringIO('<report extension="xml" type="scan" id="aaaa" content_type="text/xml" format_id="a994b278-1f62-11e1-96ac-406186ea4fc5"></report>')

        r = report_parser(xml)

        self.assertIsInstance(r, list)
        self.assertEqual(0, len(r))

    # ----------------------------------------------------------------------
    def test_report_parser_invalid_threat(self):
        xml_invalid_thread = StringIO.StringIO('''<report extension="xml" id="23327e93-b82d-4c41-9a26-ce99f15bbc63" type="scan" content_type="text/xml" format_id="a994b278-1f62-11e1-96ac-406186ea4fc5">
	<results start="1" max="148">
		<result id="685ab07e-9ac8-488e-b7b2-f3f97bd37505">
			<subnet>10.211.55.35</subnet>
			<host>10.211.55.35</host>
			<port>clm_pts (6200/tcp)</port>
			<nvt oid="1.3.6.1.4.1.25623.1.0.103185">
				<name>vsftpd Compromised Source Packages Backdoor Vulnerability</name>
				<family>Gain a shell remotely</family>
				<cvss_base>7.5</cvss_base>
				<risk_factor>High</risk_factor>
				<cve>NOCVE</cve>
				<bid>48539</bid>
				<tags>cvss_base_vector=AV:N/AC:L/Au:N/C:P/I:P/A:P</tags>
				<cert></cert>
				<xref>NOXREF</xref>
			</nvt>
			<threat>AA</threat>
			<description>
 Summary:
 vsftpd is prone to a backdoor vulnerability.

Attackers can exploit this issue to execute arbitrary commands in the
context of the application. Successful attacks will compromise the
affected application.

The vsftpd 2.3.4 source package is affected.
 Solution:
 The repaired package can be downloaded from
https://security.appspot.com/vsftpd.html. Please validate the package
with its signature.
			</description>
			<original_threat>High</original_threat>
			<notes></notes>
			<overrides></overrides>
		</result>
	</results>
</report>''')

        xml_empty_thread = StringIO.StringIO('''<report extension="xml" id="23327e93-b82d-4c41-9a26-ce99f15bbc63" type="scan" content_type="text/xml" format_id="a994b278-1f62-11e1-96ac-406186ea4fc5">
	<results start="1" max="148">
		<result id="685ab07e-9ac8-488e-b7b2-f3f97bd37505">
			<subnet>10.211.55.35</subnet>
			<host>10.211.55.35</host>
			<port>clm_pts (6200/tcp)</port>
			<nvt oid="1.3.6.1.4.1.25623.1.0.103185">
				<name>vsftpd Compromised Source Packages Backdoor Vulnerability</name>
				<family>Gain a shell remotely</family>
				<cvss_base>7.5</cvss_base>
				<risk_factor>High</risk_factor>
				<cve>NOCVE</cve>
				<bid>48539</bid>
				<tags>cvss_base_vector=AV:N/AC:L/Au:N/C:P/I:P/A:P</tags>
				<cert></cert>
				<xref>NOXREF</xref>
			</nvt>
			<threat></threat>
			<description>
 Summary:
 vsftpd is prone to a backdoor vulnerability.

Attackers can exploit this issue to execute arbitrary commands in the
context of the application. Successful attacks will compromise the
affected application.

The vsftpd 2.3.4 source package is affected.
 Solution:
 The repaired package can be downloaded from
https://security.appspot.com/vsftpd.html. Please validate the package
with its signature.
			</description>
			<original_threat>High</original_threat>
			<notes></notes>
			<overrides></overrides>
		</result>
	</results>
</report>''')

        self.assertEqual(0, len(report_parser(xml_invalid_thread)))
        self.assertEqual(0, len(report_parser(xml_empty_thread)))

    # ----------------------------------------------------------------------
    def test_report_parser_valid_vulnerability_returned_object_simple_xml(self):
        xml = StringIO.StringIO('''<report extension="xml" id="23327e93-b82d-4c41-9a26-ce99f15bbc63" type="scan" content_type="text/xml" format_id="a994b278-1f62-11e1-96ac-406186ea4fc5">
	<results start="1" max="148">
		<result id="685ab07e-9ac8-488e-b7b2-f3f97bd37505">
			<subnet>10.211.55.35</subnet>
			<host>10.211.55.35</host>
			<port>clm_pts (6200/tcp)</port>
			<nvt oid="1.3.6.1.4.1.25623.1.0.103185">
				<name>vsftpd Compromised Source Packages Backdoor Vulnerability</name>
				<family>Gain a shell remotely</family>
				<cvss_base>7.5</cvss_base>
				<risk_factor>High</risk_factor>
				<cve>NOCVE</cve>
				<bugtraq>188,999,191919,00000</bugtraq>
				<bid>48539, 43918</bid>
				<tags>cvss_base_vector=AV:N/AC:L/Au:N/C:P/I:P/A:P</tags>
				<cert></cert>
				<xref>NOXREF</xref>
			</nvt>
			<threat>High</threat>
			<description>

  Summary:
  The host is running ProFTPD and is prone to denial of service
  vulnerability.

  Vulnerability Insight:
  The flaw is due to an error in &apos;pr_data_xfer()&apos; function which allows
  remote authenticated users to cause a denial of service (CPU consumption)
  via an ABOR command during a data transfer.

  Impact:
  Successful exploitation will allow attackers to cause a denial of service.
  Impact Level: Application

  Affected Software/OS:
  ProFTPD versions prior to 1.3.2rc3

  Solution:
  Upgrade to ProFTPD version 1.3.2rc3 or later,
  For updates refer to http://www.proftpd.org/
			</description>
			<original_threat>High</original_threat>
			<notes></notes>
			<overrides></overrides>
		</result>
	</results>
</report>''')

        r = report_parser(xml)

        self.assertEqual(1, len(r))

        v = r[0]

        # Simple properties
        self.assertEqual("685ab07e-9ac8-488e-b7b2-f3f97bd37505", v.id)
        self.assertEqual("10.211.55.35", v.subnet)
        self.assertEqual("10.211.55.35", v.host)
        self.assertEqual("High", v.threat)

        # NVT
        self.assertEqual("1.3.6.1.4.1.25623.1.0.103185", v.nvt.oid)
        self.assertEqual("vsftpd Compromised Source Packages Backdoor Vulnerability", v.nvt.name)
        self.assertEqual("Gain a shell remotely", v.nvt.family)
        self.assertEqual(7.5, v.nvt.cvss_base)
        self.assertEqual("AV:N/AC:L/Au:N/C:P/I:P/A:P", v.nvt.cvss_base_vector)
        self.assertEqual([], v.nvt.xrefs)

        # Port
        self.assertEqual("tcp", v.port.proto)
        self.assertEqual("clm_pts", v.port.port_name)
        self.assertEqual(6200, v.port.number)

        # CVE, BID and XREF
        self.assertIsInstance(v.nvt.cve, list)
        self.assertEqual(0, len(v.nvt.cve))

        self.assertIsInstance(v.nvt.bid, list)
        self.assertEqual(2, len(v.nvt.bid))
        self.assertEqual(["48539", "43918"], v.nvt.bid)

        self.assertIsInstance(v.nvt.bugtraq, list)
        self.assertEqual(4, len(v.nvt.bugtraq))
        self.assertEqual(["188", "999", "191919", "00000"], v.nvt.bugtraq)

        self.assertIsInstance(v.nvt.xrefs, list)
        self.assertEqual(0, len(v.nvt.xrefs))

    def test_report_parser_valid_vulnerability_returned_object_complex_xml(self):
        r = report_parser(self.path)

if __name__ == '__main__':
    unittest.main()
