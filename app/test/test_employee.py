#!/usr/bin/env python3.6
import unittest
from app.main.service.employee_service import *
from app.main.model.employee import Employee


class TestApi(unittest.TestCase):

    def test_get_emp(self):
        self.assertTrue(isinstance(get_emp(6), (Employee, dict)))

    def test_get_emps(self):
        self.assertTrue(isinstance(get_emps(), list))

    def test_create_employee(self):
        self.assertTrue(isinstance(create_employee('xyz', 'xyz@gmail.com'), Employee))

    def test_update_emp(self):
        self.assertTrue(isinstance(update_employee(5, 'xyz1', 'xyz1@gmail.com'), (Employee, dict)))

    def test_delete_emp(self):
        self.assertTrue(isinstance(delete_emp(7), (Employee, dict)))



