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

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """ Test the public_repos property of GithubOrgClient class.
        """

        mock_repos_url = 'https://api.github.com/orgs/google/repos'

        expected_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]

        mocked_get_json.return_value = expected_repos_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = mock_repos_url

            gh_client = GithubOrgClient("google")

            self.assertEqual(gh_client.public_repos(), ["repo1", "repo2"])

            mocked_get_json.assert_called_once_with(mock_repos_url)

            mocked_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
