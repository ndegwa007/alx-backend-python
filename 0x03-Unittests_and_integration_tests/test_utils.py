#!/usr/bin/env python3
"""tests module for utils, client files"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch, PropertyMock


class TestAccessNestedMap(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, n_map, p, expected):
        """test fuction to access nested map func"""
        result = access_nested_map(n_map, p)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, p):
        """test the KeyError exception"""
        msg = "KeyError: {}".format(p)
        with self.assertRaises(KeyError) as msg:
            access_nested_map(nested_map, p)


class TestGetJson(unittest.TestCase):
    """mock the test object"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("requests.get")
    def test_get_json(self, url, res, mock_get):
        """test JSON response"""
        mock_res = Mock()
        mock_res.json.return_value = res

        mock_get.return_value = mock_res
        url_data = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(url_data, res)


class TestMemoize(unittest.TestCase):
    """test a memoize"""

    def test_memoize(self):
        """mock a_method()"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                'a_method', return_value=42) as mock_a_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, mock_a_method.return_value)
            self.assertEqual(instance.a_property, mock_a_method.return_value)
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
