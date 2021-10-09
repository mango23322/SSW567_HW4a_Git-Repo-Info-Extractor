# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation
"""

import unittest
from unittest import mock

from ExtractGitRepoInfo import extractUserData, extractCommitData

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestExtractGitRepoInfo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def mockResponse(self, json_data):
        """returns the mock response for the json data"""
        mock_response = mock.Mock()
        mock_response.json = mock.Mock(return_value = json_data) # mocks the return of requests.get
        return mock_response

    @mock.patch('requests.get')
    def testGetRepoNames(self, mockedReq):
        """test retreiving the get repos, ensure that the correct number of repos are retrieved (2)"""
        # mock the return of request.get from "https://api.github.com/users/" + user + "/repos"
        mockedReq.return_value = self.mockResponse(json_data = [{"name":"repo1"},{"name": "repo2"}])
        self.assertEqual(len(extractUserData("user")),2)

    @mock.patch('requests.get')
    def testGetCommits(self, mockedReq):
        """Test the number of commits for a repo"""
        # mock the return of request.get from "https://api.github.com/repos/" + user + "/" + name +"/commits"
        mockedReq.return_value = self.mockResponse(json_data = [{"parents":"1"},{"parents":"2"},{"parents":"3"}])
        git_dict = extractCommitData("user",{"repo1" : 0})
        self.assertEqual(git_dict["repo1"],3)

    @mock.patch('requests.get')
    def testBadUsername(self, mockedReq):
        """Test a username that does not exist"""
        # mock the return of request.get from "https://api.github.com/users/" + user + "/repos using a bad user ID"
        bad_message ={'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-repositories-for-a-user'}
        mockedReq.return_value = self.mockResponse(json_data = bad_message)
        self.assertEqual(extractUserData("badusername"),"User does not exist")

    def testwrongInputType(self):
        """Test inputting a non string as the username"""
        self.assertEqual(extractUserData(1234),"Invalid Input")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
