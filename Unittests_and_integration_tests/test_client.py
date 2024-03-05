#!/usr/bin/env python3
""" Unitest Module
"""

import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test GithubOrgClient.org.
    """
    @parameterized.expand([
        ("google", {"google", True}),
        ("abc", {"abc", True})])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Test the GithubOrgClient.org method for correct API call.
        """
        get_patch.return_value = expected
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org, expected)
        get_patch.assert_called_once_with(f'https://api.github.com/orgs/{org}')


if __name__ == '__main__':
    unittest.main()
