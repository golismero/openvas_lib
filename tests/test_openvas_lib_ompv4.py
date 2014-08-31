import unittest
from openvas_lib import OpenVASResult

from openvas_lib.ompv4 import *
from xml.etree import cElementTree as etree


class TestOMPv4(unittest.TestCase):

    def setUp(self):
        self.transform = OMPv4.transform

    # def test___init__(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     assert False  # TODO: implement your test here
    #
    # def test_create_target(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.create_target(name, hosts, comment))
    #     assert False  # TODO: implement your test here
    #
    # def test_create_task(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.create_task(name, target, config, comment))
    #     assert False  # TODO: implement your test here
    #
    # def test_delete_target(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.delete_target(target_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_delete_task(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.delete_task(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_configs(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_configs(config_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_configs_ids(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_configs_ids(name))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_html(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_report_html(report_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_id(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_report_id(scan_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_pdf(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_report_pdf(report_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_report_xml(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_report_xml(report_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_results(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_results(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_task_status(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_task_status(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_tasks(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_detail(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_tasks_detail(scan_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_ids(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_tasks_ids(name))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_ids_by_status(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_tasks_ids_by_status(status))
    #     assert False  # TODO: implement your test here
    #
    # def test_get_tasks_progress(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.get_tasks_progress(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_is_task_running(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.is_task_running(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_start_task(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.start_task(task_id))
    #     assert False  # TODO: implement your test here
    #
    # def test_stop_task(self):
    #     # o_m_pv4 = OMPv4(omp_manager)
    #     # self.assertEqual(expected, o_m_pv4.stop_task(task_id))
    #     assert False  # TODO: implement your test here


if __name__ == '__main__':
    unittest.main()
