# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program to extract github repos and # of commits 
based on an inputted username

"""
############################################

import requests
import json

############################################

def extractUserData(user):
    """
    when given a username, return a list of the users repos and the # of commits for each repo
    """
    invalidInput = 'Invalid Input'
    noUser = "User does not exist"

    repos_dict = {} # dict of repos for current user and commits for each repo

    # verify that user name is a string
    if not isinstance(user,str):
        return invalidInput

    # web address with info on users repos
    address = "https://api.github.com/users/" + user + "/repos"

    # get the data from the web address
    repos = requests.get(address)

    # repos contains a list that has an entry of data for each repository in the users account
    for i in range(len(repos.json())):
        try:
            repo_info = repos.json()[i] # holds the info on the current repo 
        # If the account does not have any repos, return appropriate text
        except:
            return noUser

        repos_dict[repo_info['name']] = 0 # add the name of the current repo to the dict

    return(repos_dict)

def extractCommitData(user, repos_dict):
    for name in repos_dict:
        # web address that contains the commits for each repo
        repo_address = "https://api.github.com/repos/" + user + "/" + name +"/commits"
        current_repo = requests.get(repo_address) # get the data from the web address
        count = current_repo.json()
        repos_dict[name] = len(count) # add the count to the dictionary

    return repos_dict

#main

invalidInput = 'Invalid Input'
noUser = "User does not exist"


while True:
    username = input("Enter the user name: ")
    data = extractUserData(username) # returns a dict with the usernames repositories

    # if the data returned has any abnormal data, print out the proper message
    if data == invalidInput:
        print(invalidInput)
    elif data == noUser:
        print(noUser)
    else:
        data = extractCommitData(username, data) # find the # of commits for each repo, add the value to the dict, return the updated dict
        for i in data:
            print(i + " : " + str(data[i])) # print the dict key and the value for the users repos and commits

