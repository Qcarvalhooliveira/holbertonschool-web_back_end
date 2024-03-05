#!/usr/bin/env python3
""" Unitest Module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import Mock, patch
import requests
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for utils.access_nested_map.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """ Test access_nested_map_exception.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test class for TestGetJson.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json and create mock test.
        """
        with patch('utils.requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            get_json_response = get_json(test_url)
            self.assertEqual(get_json_response, test_payload)
            mocked_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
