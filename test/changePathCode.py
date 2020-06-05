from os import path as Path # path info
from os import chdir as Chdir # change directory
from os import getcwd as Getcwd # get current path
import os


# TESTING:
if __name__ == "__main__":
    print(Getcwd()) # g:\TryMachineLearning\visualStudioCode\MyTry\InterviewQuestion

    # print(os.listdir()) # ['.vscode', 'resources', 'test.py', 'venv']
    # print(os.listdir()[1]) # resources

    newPath = Path.join(Getcwd(),"test")
    print(newPath) # g:\TryMachineLearning\visualStudioCode\MyTry\InterviewQuestion\test

    Chdir(newPath)

    print(Getcwd()) # g:\TryMachineLearning\visualStudioCode\MyTry\InterviewQuestion\test

    Chdir("..") # cd

    print(Getcwd()) # g:\TryMachineLearning\visualStudioCode\MyTry\InterviewQuestion


# or simple way:...........
# import os
# newPath = os.path.join(os.getcwd(),"PATH")
# os.chdir(newPath)
