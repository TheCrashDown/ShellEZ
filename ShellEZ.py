import os
import shutil

class Help:
    listCommands = []
    parseCommands = [ 'ls', 'pwd','cd ', 'cp ', 'help',
                      'mv ', 'rm ', 'rmdir ', 'mkdir ']


class ErrorTypes:
    '''
    Enum class for error types
    '''
    SYNTAX_ERROR = 1
    FILE_NOT_EXISTS_ERROR = 2
    FOLDER_NOT_EXISTS_ERROR = 3
    FILE_ALREADY_EXISTS_ERROR = 4
    FOLDER_ALREADY_EXISTS_ERROR = 5
    FOLDER_NOT_EMPTY_ERROR = 6
    PATH_NOT_EXISTS_ERROR = 7


class Messages:
    '''
    Container with different massages
    '''
    stdErrorMessage = 'OOops...\nSomething went wrong:'
    specialErrorMessages = {ErrorTypes.SYNTAX_ERROR : 
                                ('Invalid command syntax\n'
                                 + 'Use help to get list of commands'),
                            ErrorTypes.FILE_NOT_EXISTS_ERROR : 
                                'File with such name does not exist',
                            ErrorTypes.FOLDER_NOT_EXISTS_ERROR : 
                                'Folder with such name does not exist',
                            ErrorTypes.FOLDER_NOT_EMPTY_ERROR : 
                                'This folder is not empty',
                            ErrorTypes.FILE_ALREADY_EXISTS_ERROR :
                                'File with the same name already exists',
                            ErrorTypes.FOLDER_ALREADY_EXISTS_ERROR :
                                'Directory with the same name already exists',
                            ErrorTypes.PATH_NOT_EXISTS_ERROR : 
                                'Such path does not exists'}

    greeting = ('Hello there! This is ShellEZ v1.0\n'
               + 'Type help to get more information')

def printErrorMessage(errorType):
    '''
    Function that prints necessary error message
    '''
    print(Messages.stdErrorMessage)
    print(Messages.specialErrorMessages[errorType])


def parse(a):
    '''
    Function that parses the input query and recognizes
    the command or returnes error
    '''
    for cmd in Help.parseCommands:
        if a.startswith(cmd):
            return cmd, a[len(cmd):]
    return False


class Cmd:
    '''
    Class with executable commands
    '''
    def help():
        print('Actually, there is no help message now, but there will be one day')

    def makeDir(path):
        if os.path.exists(path):
            printErrorMessage(ErrorTypes.FOLDER_ALREADY_EXISTS_ERROR)
            return
        os.mkdir(path)

    def changeDir(path):
        if not os.path.exists(path):
            printErrorMessage(ErrorTypes.PATH_NOT_EXISTS_ERROR)
            return
        os.chdir(path)

    def getPath():
        print(os.getcwd())

    def getListDir():
        for dir in os.listdir(os.getcwd()):
            if os.path.isfile(dir):
                print('{:.<64}{}'.format(dir, 'file'))
            else:
                print('{:.<64}{}'.format(dir, 'folder'))

    def removeFile(path):
        if (not os.path.exists(path)) or (not os.path.isfile(path)):
            printErrorMessage(ErrorTypes.FILE_NOT_EXISTS_ERROR)
            return
        os.remove(path)

    def removeDir(path):
        if (not os.path.exists(path)) or (not os.path.isdir(path)):
            printErrorMessage(ErrorTypes.FOLDER_NOT_EXISTS_ERROR)
            return
        if len(os.listdir(path)) > 0:
            printErrorMessage(ErrorTypes.FOLDER_NOT_EMPTY_ERROR)
            return
        os.rmdir(path)

    def copyFile(arg):
        if arg.find(' ') == -1:
            printErrorMessage(ErrorTypes.SYNTAX_ERROR)
            return
        source, dest = arg.split(' ')
        #print('debug:' , end='\t')
        #print(source)
        #print('debug:' , end='\t')
        #print(dest)

        if not os.path.exists(source):
            printErrorMessage(ErrorTypes.FILE_NOT_EXISTS_ERROR)
            return

        if not os.path.exists(dest):
            printErrorMessage(ErrorTypes.PATH_NOT_EXISTS_ERROR)
            return

        shutil.copy(source, dest)

    def moveFile(arg):
        
        Cmd.copyFile(arg)

        Cmd.removeFile(source)



print(Messages.greeting)

while True:
    currentPath = os.getcwd()
    print(currentPath, '>', sep='', end=' ')
    a = input().strip(' \t')
    b = parse(a)
    if b == False:
        printErrorMessage(ErrorTypes.SYNTAX_ERROR)
    else:
        command = b[0]
        arg = b[1].strip(' \t')
        #print('debug:' , end='\t')
        #print(command, arg)
        if command.startswith('mkdir'):
            Cmd.makeDir(arg)
        elif command.startswith('cd'):
            Cmd.changeDir(arg)
        elif command.startswith('help'):
            Cmd.help()
        elif command.startswith('pwd'):
            Cmd.getPath()
        elif command.startswith('rm '):
            Cmd.removeFile(arg)
        elif command.startswith('rmdir '):
            Cmd.removeDir(arg)
        elif command.startswith('ls'):
            Cmd.getListDir()
        elif command.startswith('cp '):
            Cmd.copyFile(arg)
        elif command.startswith('mv '):
            Cmd.moveFile(arg)
