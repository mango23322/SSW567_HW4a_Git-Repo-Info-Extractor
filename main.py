# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program to extract
github repos and # of commits based on an inputted username
"""
############################################

from ExtractGitRepoInfo import extractUserData, extractCommitData

############################################

#main
INVALID_INPUT = 'Invalid Input'
NO_USER = "User does not exist"

while True:
    username = input("Enter the user name: ")
    data = extractUserData(username) # returns a dict with the usernames repositories

    # if the data returned has any abnormal data, print out the proper message
    if data == INVALID_INPUT:
        print(INVALID_INPUT)
    elif data == NO_USER:
        print(NO_USER)
    else:
        # find the # of commits for each repo, add the value to the dict, return the updated dict
        data = extractCommitData(username, data)
        for i in data:
            # print the dict key and the value for the users repos and commits
            print(i + " : " + str(data[i]))
