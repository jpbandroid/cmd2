import math
import os
from os.path import exists as file_exists
import shutil
from datetime import datetime
import platform

def mkdir(*name):
    dirname = ' '.join(name)
    os.makedirs(dirname)
def rmdir(*name):
    path = ' '.join(name)
    shutil.rmtree(path)
def delete(*name):
    path = ' '.join(name)
    os.remove(path)
def time_get():
    time_now = datetime.now()
    print(time_now)
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
def help():
    print('''All the available commands in cmd2 Beta 3:
cd - Opens a directory to be viewed in cmd2
curdate - gets the current date & time
del - delete a file from the current directory
dir - display what files and directories are inside a certain directory
exit - exits cmd2
mkdir - create a directory inside the current directory
pi - displays π
rmdir - removes a directory inside the current directory
<name of exe file> - runs an executable with the name you have inputted
help - shows you descriptions of all commands in cmd2''')
def exit(*args):
    quit()
def ver():
    print("cmd2 Version 1.0.0.3 (Beta 3)\nCopyright © 2023 jpb\nLicensed under MIT License\n\n" + platform.system(), platform.release(), platform.version())


functions = {'ver': ver, 'help': help,'curdate': time_get, 'del': delete, 'rmdir': rmdir, '': run, 'cd': cd, 'echo': echo, 'dir': dir, 'mkdir': mkdir, 'pi': pi, 'exit': exit}  # The available functions.  

print('''cmd2 [Version 1.0 BETA 3]
© 2023 jpb''')
while True:
    cwd = os.getcwd()
    command, *arguments = input(cwd + "> ").strip().split(' ')  # Take the user's input and split on spaces.
    isExist = file_exists(command)
    if command not in functions:
        if '.exe' not in command:
            command = command + '.exe'
        if isExist == True:
            run(command)
        else:
            run("C:\\Windows\\" + command)
            isExist2 = file_exists("C:\\Windows\\" + command)
            if isExist2 == False:
                run("C:\\Windows\\System32\\" + command)
                isExist3 = file_exists("C:\\Windows\\System32\\" + command)
                if isExist3 == False:
                    print("Couldn't find command", command)
    else:
        functions[command](*arguments)
