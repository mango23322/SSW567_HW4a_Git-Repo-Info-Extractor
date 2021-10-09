# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation
"""

import unittest
import json
from unittest import mock

from ExtractGitRepoInfo import extractUserData, extractCommitData

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestExtractGitRepoInfo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def mockResponse(self, json_data):
        """returns the mock response for the json data"""
        mock_response = mock.Mock()
        mock_response.json = mock.Mock(return_value = json_data)
        return mock_response

    @mock.patch('requests.get')
    def testGetRepoNames(self, mockedReq):
        """test retreiving the get repos, ensure that the correct number of repos are retrieved (2)"""
        mockedReq.return_value = self.mockResponse(json_data = [{"name":"repo1"},{"name": "repo2"}])
        self.assertEqual(len(extractUserData("user")),2)


    @mock.patch('requests.get')
    def testGetCommits(self, mockedReq):
        mockedReq.return_value = self.mockResponse(json_data = [{"parents":"1"},{"parents":"2"},{"parents":"3"}])
        x = extractCommitData("user",{"repo1" : 0})
        print (x)
"""
    # the repo 'squareD' has two commits and is not being updated so it should be static
    # so I am only focusing on this repo for this test
    def testSquareDHasTwoCommits(self): 
        self.assertEqual(extractGitData("mango23322")['SquareD'],2)

    # test the count of the number of public repos 
    def testCountOfRepos(self): 
        self.assertEqual(len(extractGitData("mango23322")),4)

    def testNotAUser(self): 
        self.assertEqual(extractGitData("ad;fjae;ifjdjfadf"),"User does not exist")   
 
    def testNotAString(self): 
        self.assertEqual(extractGitData(1234),"Invalid Input")  
"""
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

