# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program to extract github repos and # of commits 
based on an inputted username

"""
############################################

import requests
import json

############################################

def extractGitData(user):
    """
    when given a username, return the users repos and the # of commits for each repo
    """
    invalidInput = 'Invalid Input'
    noUser = "User does not exist"

    repos_dict = {} # dict of repos for current user and commits for each repo

    # verify that user name is a string
    if not(isinstance(user,str)):
        return invalidInput

    # web address with info on users repos
    address = "https://api.github.com/users/" + user + "/repos"

    # get the data from the web address
    repos = requests.get(address)

    # If the account does not have any repos, return appropriate text
    if len(repos.json()) == 0:
        return "No repos in user account"

    # repos contains a list that has an entry of data for each repository in the users account
    for i in range(len(repos.json())):
        repo_info = repos.json()[i] # holds the info on the current repo 
        repos_dict[repo_info['name']] = 0 # add the name of the current repo to the dict

    for name in repos_dict:
        # web address that contains the commits for each repo
        repo_address = "https://api.github.com/repos/" + user + "/" + name +"/commits"
        current_repo = requests.get(repo_address) # get the data from the web address
        count = current_repo.json()['commit'] # count the # of commits for the current repo
        repos_dict[name] = count # add the count to the dictionary

    return(repos_dict)

#main
while True:
    username = input("Enter the user name: ")
    data = extractGitData(username)
    #data = extractGitData('mango23322')

    for i in data:
        print(i + " : " + data[i])

