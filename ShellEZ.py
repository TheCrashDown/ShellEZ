import os
import shutil
from enum import Enum
from res import ErrorTypes, Messages


class Help:
    listCommands = []
    parseCommands = ['ls', 'pwd', 'cd ', 'cp ', 'help',
                     'mv ', 'rm ', 'rmdir ', 'mkdir ']


class FileManagerException(Exception):
    '''
    Exception 
    '''

    def __init__(self, errorType):
        print(Messages.stdErrorMessage)
        print(Messages.specialErrorMessages[errorType])


def parse(a):
    '''
    Function that parses the input query and recognizes
    the command or returnes error

    Arguments : 
        string form console

    Returns :
        False, if syntax is incorrect
        list (command, argument), if syntax is correct
    '''
    for cmd in Help.parseCommands:
        if a.startswith(cmd):
            return cmd, a[len(cmd):]
    return False


class Cmd:
    '''
    Class with executable commands
    '''
    def help(*args):
        print('Actually, there is no help message now, but there will be one day')

    def makeDir(path, *args):
        if os.path.exists(path):
            raise FileManagerException(
                ErrorTypes.FOLDER_ALREADY_EXISTS_ERROR)
            return
        os.mkdir(path)

    def changeDir(path, *args):
        if not os.path.exists(path):
            raise FileManagerException(ErrorTypes.PATH_NOT_EXISTS_ERROR)
            return
        os.chdir(path)

    def getPath(*args):
        print(os.getcwd())

    def getListDir(*args):
        for dir in os.listdir(os.getcwd()):
            if os.path.isfile(dir):
                print('{:.<64}{}'.format(dir, 'file'))
            else:
                print('{:.<64}{}'.format(dir, 'folder'))

    def removeFile(path, *args):
        if (not os.path.exists(path)) or (not os.path.isfile(path)):
            raise FileManagerException(ErrorTypes.FILE_NOT_EXISTS_ERROR)
            return
        os.remove(path)

    def removeDir(path, *args):
        if (not os.path.exists(path)) or (not os.path.isdir(path)):
            raise FileManagerException(ErrorTypes.FOLDER_NOT_EXISTS_ERROR)
            return
        if len(os.listdir(path)) > 0:
            raise FileManagerException(ErrorTypes.FOLDER_NOT_EMPTY_ERROR)
            return
        os.rmdir(path)

    def copyFile(arg, *args):
        if arg.find(' ') == -1:
            raise FileManagerException(ErrorTypes.SYNTAX_ERROR)
            return
        source, dest = arg.split(' ')

        if not os.path.exists(source):
            raise FileManagerException(ErrorTypes.FILE_NOT_EXISTS_ERROR)
            return

        if not os.path.exists(dest):
            raise FileManagerException(ErrorTypes.PATH_NOT_EXISTS_ERROR)
            return

        shutil.copy(source, dest)

    def moveFile(arg, *args):
        Cmd.copyFile(arg)
        Cmd.removeFile(source)

    executeCommand = {'mkdir': makeDir,
                      'cd': changeDir,
                      'help': help,
                      'pwd': getPath,
                      'rm': removeFile,
                      'rmdir': removeDir,
                      'ls': getListDir,
                      'cp': copyFile,
                      'mv': moveFile,
                      }

if __name__ == '__main__':

    print(Messages.greeting)

    while True:
        currentPath = os.getcwd()
        print(currentPath, '>', sep='', end=' ')
        a = input().strip()
        b = parse(a)
        if b == False:
            raise FileManagerException(ErrorTypes.SYNTAX_ERROR)
        else:
            command = b[0]
            arg = b[1].strip()

            Cmd.executeCommand[command](arg)
