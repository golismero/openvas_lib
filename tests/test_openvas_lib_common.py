import unittest

from openvas_lib.common import *


class TestGetConnector(unittest.TestCase):
    # def test_get_connector(self):
    #     # self.assertEqual(expected, get_connector(host, username, password, port, timeout))
    #     assert False  # TODO: implement your test here
    pass

class TestConnectionManager(unittest.TestCase):

    def setUp(self):
        self.c = ConnectionManager("dummy", "a", "b", 80, 0)

    def test___init__types(self):
        # connection_manager = ConnectionManager(host, username, password, port, timeout)
        self.assertRaises(TypeError, ConnectionManager, 0, None, None, None, None)
        self.assertRaises(TypeError, ConnectionManager, "dummy", 0, None, None, None)
        self.assertRaises(TypeError, ConnectionManager, "dummy", "a", 0, None, None)
        self.assertRaises(TypeError, ConnectionManager, "dummy", "a", "b", "a")
        self.assertRaises(ValueError, ConnectionManager, "dummy", "a", "b", -1)
        self.assertRaises(TypeError, ConnectionManager, "dummy", "a", "b", 80, "a")
        self.assertRaises(ValueError, ConnectionManager, "dummy", "a", "b", 80, -1)

    # --------------------------------------------------------------------------
    # xml_request_types
    # --------------------------------------------------------------------------
    def test_make_xml_request_types(self):
        self.assertRaises(TypeError, self.c.make_xml_request, 0)
        self.assertRaises(TypeError, self.c.make_xml_request, "", -1)

    def test_make_xml_request_xml_empty_status(self):
        xml = '<authentication_response status="" status_text="Authentication failed" />'
        self.assertRaises(ValueError, self.c.make_xml_request, xml)

    def test_make_xml_request_xml_invalid_status(self):
        xml = '<authentication_response status="800" status_text="Authentication failed" />'
        self.assertRaises(ServerError, self.c.make_xml_request, xml)

    def test_make_xml_request_xml_status_text_property(self):
        xml1 = '<authentication_response status="200" status_text="Authentication failed" />'
        xml2 = '<authentication_response status="400" status_text="Authentication failed" />'
        xml3 = '<authentication_response status="500" status_text="Authentication failed" />'
        r1 = self.c.make_xml_request(xml1)

        self.assertEqual("Authentication failed", r1)
        self.assertRaises(ClientError, self.c.make_xml_request, xml2)
        self.assertRaises(ServerError, self.c.make_xml_request, xml3)

    def test_make_xml_request_responses(self):
        xml1 = '<authentication_response status="200" status_text="Authentication failed" />'
        r1 = self.c.make_xml_request(xml1, xml_result=False)

        self.assertEqual(r1, "Authentication failed")

        r2 = self.c.make_xml_request(xml1, xml_result=True)

        self.assertEqual(xml1, etree.tostring(r2))

    # --------------------------------------------------------------------------
    # protocol_version
    # --------------------------------------------------------------------------
    def test_protocol_version(self):
        c = ConnectionManager("dummy", "a", "b", 80, 0)
        self.assertEqual("dummy", c.protocol_version)

    # --------------------------------------------------------------------------
    # _authenticate
    # --------------------------------------------------------------------------
    def test__authenticate_types(self):
        self.assertRaises(TypeError, self.c._authenticate, 1, "")
        self.assertRaises(TypeError, self.c._authenticate, "", 1)

    def test__authenticate_values(self):
        self.assertRaises(ValueError, self.c._authenticate, "", "")


class TestOMP(unittest.TestCase):
    pass
    # def test___init__(self):
    #     # o_m_p = OMP(omp_manager)
    #     assert False  # TODO: implement your test here
    #
    # def test_create_target(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.create_target(name, hosts, comment))
    #     assert False  # TODO: implement your test here
    #
    # def test_create_task(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.create_task(name, target, config, comment))
    #     assert False  # TODO: implement your test here
    #
    # def test_delete_target(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.delete_target(target_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_delete_task(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.delete_task(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_configs(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_configs(config_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_configs_ids(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_configs_ids(name))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_results(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_results(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_task_status(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_task_status(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_tasks(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_ids(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_tasks_ids(name))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_ids_by_status(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_tasks_ids_by_status(status))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_progress(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.get_tasks_progress(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_is_task_running(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.is_task_running(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_remote_server_version(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.remote_server_version())
    #     assert False  # TODO: implement your test here
    #
    # def test_start_task(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.start_task(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_stop_task(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.stop_task(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_transform(self):
    #     # o_m_p = OMP(omp_manager)
    #     # self.assertEqual(expected, o_m_p.transform())
    #     assert False  # TODO: implement your test here


if __name__ == '__main__':
    unittest.main()
