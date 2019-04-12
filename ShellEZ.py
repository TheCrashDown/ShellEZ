import os
import shutil
from res import ErrorTypes, Messages


class Help:
    listCommands = []
    parseCommands = ['ls', 'pwd', 'cd ', 'cp ', 'help',
                     'mv ', 'rm ', 'rmdir ', 'mkdir ', 'exit']


class FileManagerException(Exception):
    '''
    Custom exception class 
    '''

    def __init__(self, errorType):
        self.errorType = errorType


def parse(a):
    '''
    Function that parses the input query and recognizes
    the command or returnes error

    Args : 
        string form console

    Returns :
        False, if syntax is incorrect
        list (command, argument), if syntax is correct
    '''
    for cmd in Help.parseCommands:
        if a.lower().startswith(cmd):
            return cmd, a[len(cmd):]
    return False


class Cmd:
    '''
    Class with executable commands
    '''
    def help(*args):
        '''
        Help function

        Syntax : help
        '''
        print('\n')
        for cmd in sorted(Cmd.executeCommand):
            print('{: <8}{}'.format(cmd.upper(),
                                    Cmd.executeCommand[cmd].__doc__.lstrip()))
        print('\n')

    def makeDir(path, *args):
        '''
        Create new directory using absulute or relative path

        Syntax : mkdir PATH
        '''
        if os.path.exists(path):
            raise FileManagerException(
                ErrorTypes.FOLDER_ALREADY_EXISTS_ERROR)
        os.mkdir(path)

    def changeDir(path, *args):
        '''
        Switch to another directory using absulute or relative path

        Syntax : cd PATH
        '''
        if not os.path.exists(path):
            raise FileManagerException(ErrorTypes.PATH_NOT_EXISTS_ERROR)
        os.chdir(path)

    def getPath(*args):
        '''
        Show full path to current directory

        Syntax : pwd
        '''
        print(os.getcwd())

    def getListDir(*args):
        '''
        Show list of files and directories within current directory

        Syntax : ls
        '''
        print('\n')
        for dir in os.listdir(os.getcwd()):
            if os.path.isfile(dir):
                print('{:.<64}{}'.format(dir, 'file'))
            else:
                print('{:.<64}{}'.format(dir, 'folder'))
        print('\n')

    def removeFile(path, *args):
        '''
        Remove file using absulute or relative path

        Syntax : rm PATH
        '''
        if (not os.path.exists(path)) or (not os.path.isfile(path)):
            raise FileManagerException(ErrorTypes.FILE_NOT_EXISTS_ERROR)
        os.remove(path)

    def removeDir(path, *args):
        '''
        Remove directory using absulute or relative path

        Syntax : rmdir PATH
        '''
        if (not os.path.exists(path)) or (not os.path.isdir(path)):
            raise FileManagerException(ErrorTypes.FOLDER_NOT_EXISTS_ERROR)
        if len(os.listdir(path)) > 0:
            raise FileManagerException(ErrorTypes.FOLDER_NOT_EMPTY_ERROR)
        os.rmdir(path)

    def copyFile(arg, *args):
        '''
        Copy SOURCE file to DEST using absulute or relative path

        Syntax : cp SOURCE DEST
        '''
        if ' ' not in arg:
            raise FileManagerException(ErrorTypes.SYNTAX_ERROR)
        source, dest = arg.split(' ')

        if not os.path.exists(source):
            raise FileManagerException(ErrorTypes.FILE_NOT_EXISTS_ERROR)

        if not os.path.exists(dest):
            raise FileManagerException(ErrorTypes.PATH_NOT_EXISTS_ERROR)

        shutil.copy(source, dest)

    def moveFile(arg, *args):
        '''
        Move SOURCE file to DEST using absulute or relative path

        Syntax : mv SOURCE DEST
        '''
        Cmd.copyFile(arg)
        Cmd.removeFile(source)

    def exitShell(*args):
        '''
        Exit ShellEZ

        Syntax : exit
        '''
        raise SystemExit(0)

    executeCommand = {'mkdir': makeDir,
                      'cd': changeDir,
                      'help': help,
                      'pwd': getPath,
                      'rm': removeFile,
                      'rmdir': removeDir,
                      'ls': getListDir,
                      'cp': copyFile,
                      'mv': moveFile,
                      'exit' : exitShell,
                      }


# executable part
if __name__ == '__main__':

    fileManager = Cmd()

    print(Messages.greeting)

    while True:
        currentPath = os.getcwd()
        print(currentPath, '>', sep='', end=' ')
        a = input().strip()
        if a == '':
            continue
        b = parse(a)
        try:
            if b == False:
                raise FileManagerException(ErrorTypes.SYNTAX_ERROR)
            else:
                command = b[0]
                arg = b[1].strip()

                fileManager.executeCommand[command.strip()](arg)

        except FileManagerException as e:
            print(Messages.stdErrorMessage)
            print(Messages.specialErrorMessages[e.errorType])
