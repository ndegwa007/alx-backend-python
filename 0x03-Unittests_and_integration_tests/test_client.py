#!/usr/bin/env python3
"""module integrates unit tests for client.py file"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """class holds various test functions"""
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json', return_value={})
    def test_org(self, org, patched):
        """test org resp"""
        instance = GithubOrgClient(org)
        self.assertEqual(instance.org, patched.return_value)
        patched.assert_called_once()

    def test_public_repos_url(self):
        """test _public_repos_url resp"""
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock,
                return_value={
                    "repos_url": "https://api.github.com/orgs/google/repos"}
                ) as mock_repo_url:
            instance = GithubOrgClient("google")
            result = instance._public_repos_url
            self.assertEqual(result, mock_repo_url.return_value["repos_url"])

    @patch(
            'client.get_json',
            return_value={"repos_url": "http://bigBrain.url"})
    def test_public_repos(self, first_patch):
        """unit test GithubOrgClient.public_repos"""
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock,
                return_value=[]) as second_patch:
            instance = GithubOrgClient("BigBrain")
            test_repos = instance.public_repos(license="SmallBrain")
            self.assertEqual(test_repos, second_patch.return_value)
            first_patch.assert_called_once()
            second_patch.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}},
            "my_license", True),
        ({"license": {"key": "other_license"}},
            "my_license", False)
        ])
    def test_has_license(self, repo, key, expected):
        """unit test has_license"""
        instance = GithubOrgClient.has_license(repo, key)
        self.assertEqual(instance, expected)
