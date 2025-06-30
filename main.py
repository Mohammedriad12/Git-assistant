import os
import git 
from git import Repo
import argparse

# Get the name of the current file

file_path = os.path.abspath(__file__)
print(f"Current file name: {file_path}")


# parser = argparse.ArgumentParser( 
#     descripsion = "git assistent that helps execute git commands more esaly."
# )

#add function

def add_git ():
    repo = Repo.init(file_path)



#clone function

def clone_git():
    url = input("Enter the URL: ")
    Repo.clone_from(url,file_path)

#git status function
def status_git():
    