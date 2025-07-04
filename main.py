import os
import argparse
from git import Repo, GitCommandError

#add function 
def add_git(args):
    name = args.name
    path = os.getcwd()  # Get the current working directory
    file_path = os.path.join(path, name)
    if os.path.exists(file_path):
        repo = Repo(path)
        repo.git.add(file_path)
        print(f"File '{name}' added to staging area.")
    else:
        print(f"File '{name}' does not exist in the current directory: {path}. Please check the file name and try again.")

    
#____________________________________________________________________________

#clone function
def clone_git(args):
    url = args.url 
    path = args.path
    Repo.clone_from(url,path)
#____________________________________________________________________________
#git commit function
def commit_git(args):  
    repo = Repo(path)
    repo.git.add(A=True)  # Stage all changes

    commit_message = input("Enter commit message: ")
    repo.index.commit(commit_message)

    print(f"Changes committed with message: '{commit_message}'")
# git command error exception
    class GitCommandErrer(Exception):
        pass
#____________________________________________________________________________

# git status function
def status_git(args):
    path = args.path
    try:
        repo = Repo(path)
        print(repo.git.status())
    except GitCommandError as error:
        print("🛑Git Error: ", error)
    except Exception as exce:
        print("⚠ Not a Git Repo or other error", exce)
#____________________________________________________________________________
    # git log function
def log_git(args): 
    path = args.path  
    try:
        repo = Repo(path)
        for commit in repo.iter_commits():
            print(f"Commit: {commit.hexsha}, Message: {commit.message.strip()}")
    except GitCommandError as error:
        print("🛑Git Error: ", error)
    except Exception as exce:
        print("⚠ Not a Git Repo or other error", exce) 
#____________________________________________________________________________
    #git reset function
def reset_git(args):
    name = args.file
    try:
        repo = Repo(os.getcwd())
        repo.git.reset(name)
        print(f"File '{name}' has been reset in the staging area.")
    except GitCommandError as error:
        print("🛑Git Error: ", error)
    except Exception as exce:
        print("⚠ Not a Git Repo or other error", exce) 
#____________________________________________________________________________
    #git checkout function
def checkout_git(args):
    name = args.file
    try:
        repo = Repo(os.getcwd())
        repo.git.checkout(name)
        print(f"File '{name}' has been checked out.")
    except GitCommandError as error:
        print("🛑Git Error: ", error)
    except Exception as exce:
        print("⚠ Not a Git Repo or other error", exce)

#_____________________________________________________________________________
def main():
    parser = argparse.ArgumentParser( 
    description = "git assistant that helps execute git commands more esaly.")
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    subparsers.required = True

    #add function
    add_parser = subparsers.add_parser("add", help= "adding a file to staging area")
    add_parser.add_argument("name", help="a name of the local file to add")
    add_parser.set_defaults(func=add_git)

    #clone function
    clone_parser = subparsers.add_parser("clone", help= "clone file from remote repo")
    clone_parser.add_argument("url", help="remote path to add to local")
    clone_parser.add_argument("path", help="a path to the local file to add")
    clone_parser.set_defaults(func=clone_git)

    #git commit function
    commit_parser= subparsers.add_parser("commit",help="sending a local file to remote")
    commit_parser.add_argument("path",help="checking of all staging file ")
    commit_parser.add_argument("massege", help="massege to add to the commit")
    commit_parser.set_defaults(func= commit_git)

    # git status function 
    status_parser = subparsers.add_parser("status", help="check the staging area")
    status_parser.add_argument("path",help="checking of all staging file ")
    status_parser.set_defaults(func= status_git)
      
# git log function log_git
    log_parser= subparsers.add_parser("log", help= "show the history of the commits")
    log_parser.add_argument("path", help ="checking of the history ")
    log_parser.set_defaults(func=log_git)
# git reset function
    reset_parser = subparsers.add_parser("reset", help="reset the staging area")
    reset_parser.add_argument("file", help="reset the staging area")
    reset_parser.set_defaults(func=reset_git)
# git checkout function
    checkout_parser = subparsers.add_parser("checkout", help="checkout a file") 
    checkout_parser.add_argument("file", help="a file to checkout")
    checkout_parser.set_defaults(func=checkout_git) 


    
    args = parser.parse_args()
    args.func(args)

#_____________________________________________________________________________
if __name__ == '__main__':
    main()
