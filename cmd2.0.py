import math
import os

def mkdir(*name):
    dirname = ' '.join(name)
    os.makedirs(dirname)
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
def exit(*args):
    quit()


functions = {'cd': cd, 'echo': echo, 'dir': dir, 'mkdir': mkdir, 'pi': pi, 'exit': exit}  # The available functions.  

print('''cmd2 [Version 1.0 BETA 1]
© 2023 jpb''')
while True:
    cwd = os.getcwd()
    command, *arguments = input(cwd + "> ").strip().split(' ')  # Take the user's input and split on spaces.
    if command not in functions:
        print("Couldn't find command", command)
    else:
        functions[command](*arguments)
