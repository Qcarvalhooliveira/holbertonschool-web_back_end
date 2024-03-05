#!/usr/bin/env python3
""" Unitest Module
"""

import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ Test that the _public_repos_url property returns the expected URL.
        """
        expected_url = 'https://api.github.com/orgs/google/repos'
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value={'repos_url': expected_url})):
            gh_client = GithubOrgClient("google")
            self.assertEqual(gh_client._public_repos_url, expected_url)


if __name__ == '__main__':
    unittest.main()
