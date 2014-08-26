import unittest


class TestSetInterval(unittest.TestCase):  # TODO
    def test_set_interval(self):
        # self.assertEqual(expected, set_interval(interval, times))
        assert False # TODO: implement your test here


class TestGenerateRandomString(unittest.TestCase):  # TODO
    def test_generate_random_string(self):
        # self.assertEqual(expected, generate_random_string(length))
        assert False # TODO: implement your test here


class TestVulnscanManager(unittest.TestCase):  # TODO
    def test___init__(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        assert False # TODO: implement your test here

    def test_delete_scan(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.delete_scan(task_id))
        assert False # TODO: implement your test here

    def test_delete_target(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.delete_target(target_id))
        assert False # TODO: implement your test here

    def test_get_all_scans(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.get_all_scans())
        assert False # TODO: implement your test here

    def test_get_finished_scans(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.get_finished_scans())
        assert False # TODO: implement your test here

    def test_get_profiles(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.get_profiles())
        assert False # TODO: implement your test here

    def test_get_progress(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.get_progress(task_id))
        assert False # TODO: implement your test here

    def test_get_results(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.get_results(task_id))
        assert False # TODO: implement your test here

    def test_get_running_scans(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.get_running_scans())
        assert False # TODO: implement your test here

    def test_launch_scan(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.launch_scan(target, **kwargs))
        assert False # TODO: implement your test here

    def test_stop_audit(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.stop_audit(task_id))
        assert False # TODO: implement your test here

    def test_target_id(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.target_id())
        assert False # TODO: implement your test here

    def test_task_id(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.task_id())
        assert False # TODO: implement your test here

    def test_transform(self):
        # vulnscan_manager = VulnscanManager(host, user, password, port, timeout)
        # self.assertEqual(expected, vulnscan_manager.transform(version))
        assert False # TODO: implement your test here


class test__ErrorResponse(unittest.TestCase):  # TODO
    def test___init__(self):
        # __error_response = _ErrorResponse(msg, *args)
        assert False # TODO: implement your test here

    def test___str__(self):
        # __error_response = _ErrorResponse(msg, *args)
        # self.assertEqual(expected, __error_response.__str__())
        assert False # TODO: implement your test here


class TestResultError(unittest.TestCase):  # TODO
    def test___str__(self):
        # result_error = ResultError()
        # self.assertEqual(expected, result_error.__str__())
        assert False # TODO: implement your test here


class test__ConnectionManager(unittest.TestCase):  # TODO
    def test___init__(self):
        # __connection_manager = _ConnectionManager(host, username, password, port, timeout)
        assert False # TODO: implement your test here

    def test_close(self):
        # __connection_manager = _ConnectionManager(host, username, password, port, timeout)
        # self.assertEqual(expected, __connection_manager.close())
        assert False # TODO: implement your test here

    def test_make_xml_request(self):
        # __connection_manager = _ConnectionManager(host, username, password, port, timeout)
        # self.assertEqual(expected, __connection_manager.make_xml_request(xmldata, xml_result))
        assert False # TODO: implement your test here

    def test_protocol_version(self):
        # __connection_manager = _ConnectionManager(host, username, password, port, timeout)
        # self.assertEqual(expected, __connection_manager.protocol_version())
        assert False # TODO: implement your test here


class test__OMP(unittest.TestCase):  # TODO
    def test___init__(self):
        # __om_p = _OMP(omp_manager)
        assert False # TODO: implement your test here

    def test_create_target(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.create_target(name, hosts, comment))
        assert False # TODO: implement your test here

    def test_create_task(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.create_task(name, target, config, comment))
        assert False # TODO: implement your test here

    def test_delete_target(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.delete_target(target_id))
        assert False # TODO: implement your test here

    def test_delete_task(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.delete_task(task_id))
        assert False # TODO: implement your test here

    def test_get_configs(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_configs(config_id))
        assert False # TODO: implement your test here

    def test_get_configs_ids(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_configs_ids(name))
        assert False # TODO: implement your test here

    def test_get_results(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_results(task_id))
        assert False # TODO: implement your test here

    def test_get_tasks(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_tasks(task_id))
        assert False # TODO: implement your test here

    def test_get_tasks_ids(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_tasks_ids(name))
        assert False # TODO: implement your test here

    def test_get_tasks_ids_by_status(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_tasks_ids_by_status(status))
        assert False # TODO: implement your test here

    def test_get_tasks_progress(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.get_tasks_progress(task_id))
        assert False # TODO: implement your test here

    def test_remote_server_version(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.remote_server_version())
        assert False # TODO: implement your test here

    def test_start_task(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.start_task(task_id))
        assert False # TODO: implement your test here

    def test_stop_task(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.stop_task(task_id))
        assert False # TODO: implement your test here

    def test_transform(self):
        # __om_p = _OMP(omp_manager)
        # self.assertEqual(expected, __om_p.transform())
        assert False # TODO: implement your test here


class test__OMPv4(unittest.TestCase):  # TODO
    def test___init__(self):
        # __om_pv4 = _OMPv4(omp_manager)
        assert False # TODO: implement your test here

    def test_create_target(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.create_target(name, hosts, comment))
        assert False # TODO: implement your test here

    def test_create_task(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.create_task(name, target, config, comment))
        assert False # TODO: implement your test here

    def test_delete_target(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.delete_target(target_id))
        assert False # TODO: implement your test here

    def test_delete_task(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.delete_task(task_id))
        assert False # TODO: implement your test here

    def test_get_configs(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_configs(config_id))
        assert False # TODO: implement your test here

    def test_get_configs_ids(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_configs_ids(name))
        assert False # TODO: implement your test here

    def test_get_results(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_results(task_id))
        assert False # TODO: implement your test here

    def test_get_tasks(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_tasks(task_id))
        assert False # TODO: implement your test here

    def test_get_tasks_ids(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_tasks_ids(name))
        assert False # TODO: implement your test here

    def test_get_tasks_ids_by_status(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_tasks_ids_by_status(status))
        assert False # TODO: implement your test here

    def test_get_tasks_progress(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.get_tasks_progress(task_id))
        assert False # TODO: implement your test here

    def test_start_task(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.start_task(task_id))
        assert False # TODO: implement your test here

    def test_stop_task(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.stop_task(task_id))
        assert False # TODO: implement your test here

    def test_transform(self):
        # __om_pv4 = _OMPv4(omp_manager)
        # self.assertEqual(expected, __om_pv4.transform())
        assert False # TODO: implement your test here

if __name__ == '__main__':
    unittest.main()
