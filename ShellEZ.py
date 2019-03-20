import os

class Help:
    listCommands = []
    parseCommands = [ 'ls', 'pwd','cd', 'cp', 'help'
                      'mv', 'rm', 'rmdir', 'mkdir']


class ErrorTypes:
    '''
    Enum class for error types
    '''
    SyntaxError = 1


class ErrorMessages:
    '''
    Container with error massages
    '''
    stdErrorMessage = 'OOops...\nSomething went wrong:'
    specialMessages = {ErrorTypes.SyntaxError : 'Invalid command syntax\nUse help to get list of commands'}


def printErrorMessage(errorType):
    '''
    Function that prints necessary error message
    '''
    print(ErrorMessages.stdErrorMessage)
    print(ErrorMessages.specialMessages[errorType])


def parse(a):
    '''
    Function that parses the input query and recognizes
    the command or returnes error
    '''
    for cmd in Help.parseCommands:
        if a.startswith(cmd + ' '):
            return cmd, a[len(cmd) + 1:]
    return False


def cmdHelp():
    pass


while True:
    print('>>>', end=' ')
    a = input()
    b = parse(a)
    if b == False:
        printErrorMessage(ErrorTypes.SyntaxError)
    else:
        print(b)

