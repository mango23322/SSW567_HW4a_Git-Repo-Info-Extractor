# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program to
extract github repos and # of commits based on an inputted username
"""
############################################

import requests

############################################

def extractUserData(user):
    """
    when given a username, return a list of the users repos and the # of commits for each repo
    """
    invalid_input = 'Invalid Input'
    no_user = "User does not exist"
    x = 5

    repos_dict = {} # dict of repos for current user and commits for each repo

    # verify that user name is a string
    if not isinstance(user,str):
        return invalid_input

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
            return no_user

        repos_dict[repo_info['name']] = 0 # add the name of the current repo to the dict

    return repos_dict

def extractCommitData(user, repos_dict):
    """add the # of commits for each repo to the repo dict, return the updated dict"""
    for name in repos_dict:
        # web address that contains the commits for each repo
        repo_address = "https://api.github.com/repos/" + user + "/" + name +"/commits"
        current_repo = requests.get(repo_address) # get the data from the web address
        count = current_repo.json()
        repos_dict[name] = len(count) # add the count to the dictionary

    return repos_dict
