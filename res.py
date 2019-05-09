from enum import Enum

APP_VERSION = 1.3.2.1

class ErrorTypes(Enum):
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
    specialErrorMessages = {ErrorTypes.SYNTAX_ERROR:
                            ('Invalid command syntax\n'
                             'Use help to get list of commands'),
                            ErrorTypes.FILE_NOT_EXISTS_ERROR:
                                'File with such name does not exist',
                            ErrorTypes.FOLDER_NOT_EXISTS_ERROR:
                                'Folder with such name does not exist',
                            ErrorTypes.FOLDER_NOT_EMPTY_ERROR:
                                'This folder is not empty',
                            ErrorTypes.FILE_ALREADY_EXISTS_ERROR:
                                'File with the same name already exists',
                            ErrorTypes.FOLDER_ALREADY_EXISTS_ERROR:
                                'Directory with the same name already exists',
                            ErrorTypes.PATH_NOT_EXISTS_ERROR:
                                'Such path does not exists'}

    greeting = ('Hello there! This is ShellEZ v' + str(APP_VERSION) + '\n'
                'Type help to get more information')
