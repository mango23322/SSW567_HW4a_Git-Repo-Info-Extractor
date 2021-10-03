# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation
"""

import unittest

from ExtractGitRepoInfo import extractGitData

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestExtractGitRepoInfo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

# my repo, # of repos
# my repo, specific repo / number of commits
# bad username
# empty repo?
# not a string


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

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

