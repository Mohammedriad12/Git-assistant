# Get the name of the current file
file_path = os.path.abspath(__file__)
print(f"Current file name: {file_path}")


# #add function
def add_git ():
    repo = Repo.init(file_path)



 #clone function
def clone_git():
    url = input("Enter the URL: ")
    Repo.clone_from(url,file_path)

# #git status function

 def status_git():
    repo = Repo(file_path)
    status = repo.git.status()
    print("Git Status:")
    print(status)


#git commit function
def commit_git():
    repo = Repo(file_path)
    repo.git.add(A=True)  # Stage all changes
    commit_message = input("Enter commit message: ")
    repo.index.commit(commit_message)
    print(f"Changes committed with message: '{commit_message}'")

# status_git()
def status_git():
    try:
        repo = Repo(file_path   )
        print(repo.git.status())
    except GitCommandErrer as error:
        print("🛑Git Errer: ",error)
    except Exception as exce:
        print("⚠ Not a Git Repo or other error",exce)


____________________________________________________________________________
import os
from git import Repo, GitCommandError

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser( 
    descripsion = "git assistant that helps execute git commands more esaly."
    )
    # remote repo path
    parser.add_argument(
        "-u","-url", metavar="remote url",
        required=True, help="pass in the url of the remote repo"
    )
    # local path
    parser.add_argument(
        "-p","--path", metavar = "local path",
        required=True, help="pass in the local file path"
    )
    # branch name
    parser.add_argument(
        "-b","--branch", metavar="barch name",
        required=True, help="pass in the branches names"
    )
    # file name
    parser.add_argument(
        "-f","--file",metavar="local name",
        required=True, help= "pass in the local file name"
    )
    # massege
    parser.add_argument(
        "-m","--massege", metavar="massege",
        required=True, help=" pass in the massege to send"
    )