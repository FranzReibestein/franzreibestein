## 2. Homework + Review

#2.1 Vocabulary Review
"""
Git vs. GitHub 

Git a version control tool that is installed on my computer. It tracks changes to files in a local repository.
GitHub is a website which allows me to save my local Git repository in a remote GitHub repository.

Terminal vs. Command Line
The terminal is a window in which I can type text commands and see the respective output of the commands.
The command line is a part of the terminal in which I type text commands.

Local vs. Remote Repository
A local repository is saved only on my computer, whereas a remote repository is saved online.

Version Control
A system (like Google drive) that tracks the history of files/repositories.


Staging Area
I can upload the the version history of a file/repository from my local Git repository to a remote GitHub repository.
In the uploading process, the staging area is the first step in which I collect the changes to my files/repositories I want
to upload to GitHub.

git add
This command moves changes to the staging area.

git commit
This command saves the staged changes as a snapshot to the local Git repository's history.

git push
This command uploads the latest snapshots saved in the local Git repository into my remote GitHub repo.

git status
Shows the current status of my local repository and of the staging area relative to the last commit. 


git pull
Downloads new commits from a GitHub repository and merges them into the curretn branch of my local Git repo.

pwd
prints the current working directory

ls
lists the files and directories in my current working directory

cd
changes the working directory

nano
opens a text editor in the terminal that allows me to edit text files

touch
creates a new empty file

mv
moves a file or repo to another repo or renames the repo/file

rm
The remove command removes files from the current working directory.


cat
prints the contents of a file.

"""

'''
2.2 A directory tree
Questions

You have been plopped into Judy’s directory system. What command will tell you what your
current working directory is?
pwd

The terminal responds by saying you are in ∼/python decal/judy decal. What command
will list all the files in your current working directory?

ls -a

Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
You will need to pull the brianna repo repository to find the updated file. What command(s)
will let you move to the correct repository and pull the latest changes?
changing the directory: cd ~/python_decal/brianna_repo
pulling the latest changes: git pull origin main

How would you move this new homework.py to the homework/ folder in your personal repository?
mv homework.py ../judy_decal/homework

How would you move yourself to the same repository as homework.py?
cd ../judy_decal/homework


You want to see the contents of homework.py in your terminal, how would you do this?
cat homework.py

Great job! You just finished the homework for this week. What command(s) allow you to
save the changes and push from your local repository to your remote repository?

change the wd to the judy_decal directory: cd ..
git add .
git commit -m "done with the homework"
git push origin main

Oh no! Git gave you the following error. What commands should you call to resolve this
error and push your homework properly? What does the error mean? (i.e. what did “Judy”
do wrong when trying to push?)

#the problem is that the remote repository contains changes (commits) that the local repository does not have.
Therefore, pushing the local repo would overwrite these locally non-existing commits, that's why
GitHub refuses the push.
Resolving the error involves pulling properly (git pull origin main), first, which merges the new remote commits from the remote GitHub repo
into the actual branch of the local Git repo. Now, the local Git repo has the same version history as the
remote GitHub repo. When we type git push origin main now, this should be succesfull.

What absolute path will allow you to move to Recents/?
cd ~/Recent
'''

##3. Homework Review
#3.1 Data Types
def checkDataType(argument):
    t = type(argument).__name__
    return t

#3.2
def evenOrOdd(number):
    if number % 2 == 0:
        return "Even"
    else: 
        return "Odd"

#4. Loops
def loopsum(l):
    total=0
    for i in l:
        total +=i
    return total

#5 Homework 4 Review
#5.1 Lists
#Write a function that takes a list and returns a new list with each element duplicated.

def duplicateList(l):
    leng = len(l) #gets the number of elements in the list
    container = [None]*(2*leng) #creates a list twice the length og the argument list with None values 
    for i in range(leng): #loop over the indices of the elements in the argument list
        container[2*i] =l[i] #fill the container with duplicates 
        container[2*i+1] = l[i] #fill the container with duplicates 
    return container

#5.2 debugging
#def square(num)
#return num * num
# there is a colon missing after square(num). inserting the colon should suffice to fix the error

def square(num):
    return num * num

print(duplicateList(['a', 'b', 'c']))

