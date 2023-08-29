#!/usr/bin/env python3
"""Module for test_utils.py"""
import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for parameterized functions"""
    @parameterized.expand([
        ({"a": 1}, ("a",),  1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test case for access_nested_map function"""
        output = utils.access_nested_map(nested_map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test case for access_nested_map_exception function"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
