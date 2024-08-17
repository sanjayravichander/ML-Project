import sys # The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. It's used here to get detailed information about exceptions.

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #  The traceback object, which contains information about the call stack at the point where the exception occurred.
    file_name=exc_tb.tb_frame.f_code.co_filename # This retrieves the filename where the error occurred from the traceback object.
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    ) # This retrieves the line number in the script where the error occurred.
    # str(error)-This converts the error message to a string.
    # This(error_message)constructs a formatted error message string that includes the script name, line number, and the actual error message.
    return error_message

class CustomException(Exception): # This defines a custom exception class that inherits from Python's built-in Exception class. It's used to create exceptions with more detailed error messages.
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message