#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def setUp(self):
        self.test_list = [1, 2, 3, 4, 182, 532, 0, -123425, 83]

    def tearDown(self) -> None:
        pass

    def test_max_integer(self):
        """Test the max_integer function"""
        self.assertEqual(max_integer(self.test_list), 532)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)

    def test_non_list_parameter(self):
        """Test a non-list parameter"""
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_module_doc(self):
        """Test if module has documentation"""
        doc = __import__('6-max_integer').__doc__
        # print(len(doc))
        self.assertGreaterEqual(len(doc), 2)

    def test_function_doc(self):
        """Test if function 'max-integer' has documentation"""
        doc = max_integer.__doc__
        # print(len(doc))
        self.assertGreaterEqual(len(doc), 2)
