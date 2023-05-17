import math
import os
from os.path import exists as file_exists
import shutil

def mkdir(*name):
    dirname = ' '.join(name)
    os.makedirs(dirname)
def rmdir(*name):
    path = ' '.join(name)
    shutil.rmtree(path)
def delete(*name):
    path = ' '.join(name)
    print(path)
    os.remove(path)
def dir(path = None):
    if path == "":
        cwd = os.getcwd()
        dir_list = os.listdir(cwd)
        dir_list = os.listdir(cwd)
    else:
        dir_list = os.listdir(path)
        print('\n'.join(dir_list))
def pi():
    print(math.pi)
def echo(*text):
    print(' '.join(text))
def cd(path):
    os.chdir(path)
def run(path):
    os.system(path)
def exit(*args):
    quit()


functions = {'del': delete, 'rmdir': rmdir, '': run, 'cd': cd, 'echo': echo, 'dir': dir, 'mkdir': mkdir, 'pi': pi, 'exit': exit}  # The available functions.  

print('''cmd2 [Version 1.0 BETA 2]
© 2023 jpb''')
while True:
    cwd = os.getcwd()
    command, *arguments = input(cwd + "> ").strip().split(' ')  # Take the user's input and split on spaces.
    isExist = file_exists(command)
    if isExist == True:
        run(command)
    else:
        run("C:\\Windows\\" + command)
        isExist2 = file_exists("C:\\Windows\\" + command)
        if isExist2 == False:
            run("C:\\Windows\\System32\\" + command)
            isExist3 = file_exists("C:\\Windows\\System32\\" + command)
            if isExist3 == False:
                if command not in functions:
                    print("Couldn't find command", command)
                else:
                    functions[command](*arguments)
